from itertools import combinations

with open("2024/8/input.txt") as f:
    lines = [line.strip() for line in f]

antennas = {}
for y, line in enumerate(lines):
    for x, space in enumerate(line):
        if space != '.':
            antennas.setdefault(space, []).append((x, y))

x_max = len(lines[0])
y_max = len(lines)

antinodes = set()
for values in antennas.values():
    for (x1, y1), (x2, y2) in combinations(values, 2):
        sym_points = [
            (2 * x1 - x2, 2 * y1 - y2),  
            (2 * x2 - x1, 2 * y2 - y1)   
        ]
        for x, y in sym_points:
            if 0 <= x < x_max and 0 <= y < y_max:
                antinodes.add((x, y))

print(len(antinodes))
