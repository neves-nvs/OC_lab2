from math import log
with open("out", "r") as f:
    data = f.read().split("\n")[1:-1]

res = {}


class Data():
    def __init__(self, line):
        line = line.split("\t")
        self.size = int(line[0])
        self.stride = int(line[1])
        self.elapsed = float(line[2])
        self.cycles = int(line[3])

    def __repr__(self):
        return "{}\t{}\t{}\t{}\n".format(self.size, self.stride, self.elapsed, self.cycles)


for line in data:
    if int(line.split("\t")[0]) in res.keys():
        res[int(line.split("\t")[0])].append(Data(line))
    else:
        res[int(line.split("\t")[0])] = [Data(line)]


r = []
for i in res.keys():
    access = 100 * i * log(i, 2)
    m = 0
    for k in res[i]:
        m += k.elapsed
    mean = (pow(10, 9)*m) / access
    print("cache_size: {}\tt1-t2: {}\t#access: {}\t#mean: {}".format(i,
          round(m, 7), access, mean))
    r.append(mean)

import matplotlib.pyplot as plt

for i in res.keys():
    plt.plot(list(map(lambda x: x.elapsed, res[i])), label=str(i>>10)+"k")
    plt.legend()

plt.show()

