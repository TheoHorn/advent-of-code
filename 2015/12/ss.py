import re

with open("2015/12/input.txt", "r") as f:
    content = f.read()
    numbers = re.findall(r'-?\d+', content)
    print(sum(map(int, numbers)))