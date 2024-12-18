import re
from collections import Counter

with open("2016/4/input.txt") as f:
    lines = f.readlines()
    rooms = []
    for line in lines:
        match = re.match(r"([a-z-]+)-(\d+)\[([a-z]+)\]", line.strip())
        if match:
            name, sector_id, checksum = match.groups()
            rooms.append((name, int(sector_id), checksum))

sum_room = 0
for room in rooms:
    alpha = room[0]
    alpha = alpha.replace('-', '')
    counts = Counter(alpha)
    values = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    top_five = ''.join([x[0] for x in values[:5]])
    if top_five == room[2]:
        sum_room += room[1]

print(sum_room)