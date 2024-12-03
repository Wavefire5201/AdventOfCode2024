import re

# regex = r"mul\(\d{1,3},\d{1,3}\)"  # for p1
regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"  # for p2

with open("input.txt", "r") as f:
    total = 0
    do = True
    for line in f.readlines():
        matches = re.findall(regex, line)
        for match in matches:
            if "mul" in match and do:
                nums = re.findall(r"\d{1,3}", match)
                total += int(nums[0]) * int(nums[1])
            elif "don't()" in match:
                do = False
            elif "do()" in match:
                do = True

    print(total)
