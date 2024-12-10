import sys
sys.setrecursionlimit(2000)

def reach_top(array, position, visited):
    x, y = position

    if not (0 <= x < len(array[0]) and 0 <= y < len(array)):
        return set()

    if position in visited:
        return set()

    visited.add(position)

    if array[y][x] == 9:
        return {position}

    nines = set()
    current_value = array[y][x]

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < len(array[0]) and 0 <= ny < len(array) and array[ny][nx] == current_value + 1):
            nines.update(reach_top(array, (nx, ny), visited))

    return nines

with open("2024/10/input.txt") as f:
    lines = f.readlines()
    array = []
    zeroes = set()
    for y, line in enumerate(lines):
        row = []
        line = line.strip()
        for x, val in enumerate(line):
            value = int(val)
            if value == 0:
                zeroes.add((x, y))
            row.append(value)
        array.append(row)

# Count unique paths
count = 0
for zero in zeroes:
    visited = set()
    count += len(reach_top(array, zero, visited))

print(count)
