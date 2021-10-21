#!/usr/bin/env python3

import matplotlib.pyplot as plt

with open("cm1.out") as f:
    data = f.read().split("\n")[:-1]


class Data():
    def __init__(self, line):
        line = line.split()
        self.size = int(line[0].split("=")[1])
        self.stride = int(line[1].split("=")[1])
        self.misses = float(line[2].split("=")[1])
        self.time = float(line[3].split("=")[1])

    def __repr__(self):
        return "{}\t{}\t{}".format(self.stride, self.misses, self.time)


res = {}

for line in data:
    key = int(line.split()[0].split("=")[1])
    if key in res.keys():
        res[key].append(Data(line))
    else:
        res[key] = [Data(line)]

for k in res:
    print("Array Size: {}".format(k))
    print("Stride\tMisses\tTime")
    for data in res[k]:
        print(data)


for k in res:
    strides = list(map(lambda x: x.stride, res[k]))
    misses = list(map(lambda x: x.misses, res[k]))
    plt.plot(strides, misses, label=str(k >> 10)+"k")
    plt.legend()
    plt.xscale("log", basex=2)

#plt.savefig("cm1L1Plots/cm1 L1 - 1")
plt.show()
