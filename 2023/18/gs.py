from collections import deque

# Read and parse instructions once
instructions = []
with open('2023/18/input.txt') as file:
    for line in file:
        _, _, hexa = line.split(" ")
        hexa = hexa.strip()[2:]  # Remove '0x' prefix
        hexa_steps = hexa[:-2]
        hexa_dir = hexa[-2]
        steps = int("0x" + hexa_steps, 0)
        direction = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}.get(hexa_dir, 'U')
        instructions.append((direction, steps))

# Determine if a tile has been dug by simulating the path
def is_dug(x, y):
    cur_x, cur_y = 0, 0
    if (x, y) == (0, 0):
        return True
    
    for direction, steps in instructions:
        dx, dy = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}[direction]
        for _ in range(steps):
            cur_x, cur_y = cur_x + dx, cur_y + dy
            if (cur_x, cur_y) == (x, y):
                return True
    return False

# Determine bounding box
min_x, max_x, min_y, max_y = 0, 0, 0, 0
cur_x, cur_y = 0, 0
for direction, steps in instructions:
    dx, dy = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}[direction]
    for _ in range(steps):
        cur_x, cur_y = cur_x + dx, cur_y + dy
        min_x = min(min_x, cur_x)
        max_x = max(max_x, cur_x)
        min_y = min(min_y, cur_y)
        max_y = max(max_y, cur_y)

# Flood-fill BFS using only visited tracking
queue = deque()
visited = set()

# Initialize border tiles for BFS
for x in range(min_x, max_x + 1):
    for y in (min_y, max_y):
        if not is_dug(x, y):
            queue.append((x, y))
            visited.add((x, y))

for y in range(min_y, max_y + 1):
    for x in (min_x, max_x):
        if not is_dug(x, y):
            queue.append((x, y))
            visited.add((x, y))

# Flood-fill BFS
flood_filled_area = 0

while queue:
    cx, cy = queue.popleft()
    flood_filled_area += 1
    
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = cx + dx, cy + dy
        if (
            min_x <= nx <= max_x
            and min_y <= ny <= max_y
            and (nx, ny) not in visited
            and not is_dug(nx, ny)
        ):
            visited.add((nx, ny))
            queue.append((nx, ny))

# Calculate and print the result
total_area = (max_x - min_x + 1) * (max_y - min_y + 1)
result = total_area - flood_filled_area
print(result)
