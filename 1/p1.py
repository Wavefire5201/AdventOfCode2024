with open("input.txt", "r") as f:
    l = []
    r = []
    for line in f.readlines():
        t = line.split()
        l.append(int(t[0]))
        r.append(int(t[1]))

    l.sort()
    r.sort()
    total = 0
    for i in range(len(l)):
        total += abs(l[i] - r[i])

    print(total)
