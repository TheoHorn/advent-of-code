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


antinodes = set((x, y) for positions in antennas.values() for x, y in positions)
for values in antennas.values():
    for (x1, y1), (x2, y2) in combinations(values, 2):
        scale = 1
        while True:
            sym_points = [
                (x1 + scale * (x1 - x2), y1 + scale * (y1 - y2)),  # (x1, y1) as center
                (x2 + scale * (x2 - x1), y2 + scale * (y2 - y1))   # (x2, y2) as center
            ]
            
            valid_points = [
                (x, y) for x, y in sym_points
                if 0 <= x < x_max and 0 <= y < y_max
            ]
            
            if not valid_points:
                break 
            
            antinodes.update(valid_points)
            scale += 1 

print(len(antinodes))
