import re

with open("2024/3/input.txt") as f:
    content = f.read()
    data = re.findall(r"mul\((\d+),(\d+)\)", content)
    summed = 0
    for a, b in data:
        summed += int(a) * int(b)
    print(summed)