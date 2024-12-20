from collections import deque

# Read the input file
with open("2024/20/input.txt") as f:
    lines = f.readlines()
    walls = set()

    for x, line in enumerate(lines):
        for y, char in enumerate(line.strip()):
            if char == '#':
                walls.add((x, y))
            elif char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)


# Define BFS
def bfs(start):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distances = {start : 0}
    queue = deque([start])
    while queue:
        x,y = queue.popleft()
        d = distances[(x,y)]
        for direction in directions:
            nx,ny = x+direction[0], y+direction[1]
            if (nx,ny) not in distances and (nx,ny) not in walls:
                queue.append((nx,ny))
                distances[(nx,ny)] = d+1
    return distances

# Fund possible paths
cheats = {}
default = bfs(start)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for x,y in default:
    for direction in directions:
        nx,ny = x + direction[0] * 2, y + direction[1] *2
        if (nx,ny) in default and default[(nx,ny)] < default[(x,y)]:
            saved_cost = default[(x,y)] - default[(nx,ny)] - 2 
            if saved_cost > 0:
                cheats[((x,y),(nx,ny))] = saved_cost

count = 0
for cheat in cheats.values():
    if cheat >= 100 : count +=1
print(count)