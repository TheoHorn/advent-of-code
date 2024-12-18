import re

with open("2016/7/input.txt") as f:
    lines = f.readlines()


def has_abba(segment):
    return any(segment[i] != segment[i + 1] and segment[i] == segment[i + 3] and segment[i + 1] == segment[i + 2]
               for i in range(len(segment) - 3))


sumdouble = 0
for line in lines:
    parts = re.split(r'\[|\]', line.strip())
    outside = parts[0::2] 
    inside = parts[1::2]  

    if any(has_abba(segment) for segment in outside):
        if not any(has_abba(segment) for segment in inside):
            sumdouble += 1

print(sumdouble)
