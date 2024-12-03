from p1 import *

with open("input.txt", "r") as f:
    safe = 0
    for line in f.readlines():
        r = list(map(int, line.split()))
        if (inc(r) or dec(r)) and adj(r):
            safe += 1
        else:
            for i in range(len(r)):
                t = r[:i] + r[i + 1 :]
                if (inc(t) or dec(t)) and adj(t):
                    safe += 1
                    break

    print(safe)
