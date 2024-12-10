import sys
sys.setrecursionlimit(2000)

def reach_top(array, position, current_path, paths):
    x, y = position

    if not (0 <= x < len(array[0]) and 0 <= y < len(array)):
        return 0

    # Avoid cycles
    if position in current_path:
        return 0

    current_path.append(position)

    if array[y][x] == 9:
        paths.add(tuple(current_path))
        current_path.pop() 
        return 1

    current_value = array[y][x]
    path_count = 0

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < len(array[0]) and 0 <= ny < len(array) and array[ny][nx] == current_value + 1):
            path_count += reach_top(array, (nx, ny), current_path, paths)

    # Backtrack
    current_path.pop()
    return path_count


# Read the input
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


total_paths = 0
for zero in zeroes:
    paths = set()
    path_count = reach_top(array, zero, [], paths)
    total_paths += path_count

print(total_paths)
