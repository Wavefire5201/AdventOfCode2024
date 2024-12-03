def inc(r: list) -> bool:
    for i in range(1, len(r)):
        if not r[i] > r[i - 1]:
            return False

    return True


def dec(r: list) -> bool:
    for i in range(1, len(r)):
        if not r[i] < r[i - 1]:
            return False

    return True


def adj(r: list) -> bool:
    for i in range(1, len(r)):
        diff = abs(r[i] - r[i - 1])
        if diff < 1 or diff > 3:
            return False

    return True


with open("input.txt", "r") as f:
    safe = 0
    for line in f.readlines():
        r = list(map(int, line.split()))
        if (inc(r) or dec(r)) and adj(r):
            safe += 1

    print(safe)
