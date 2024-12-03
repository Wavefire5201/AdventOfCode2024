with open("input.txt", "r") as f:
    freq = {}
    l = []
    r = []
    for line in f.readlines():
        t = line.split()
        l.append(int(t[0]))
        r.append(int(t[1]))

    total = 0
    for i in l:
        total += i * r.count(i)

    print(total)
