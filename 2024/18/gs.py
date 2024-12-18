from collections import deque

with open("2024/18/input.txt") as f:
    walls = []
    lines = f.readlines()
    for line in lines:
        pos = line.split(",")
        walls.append((int(pos[0]), int(pos[1])))

def bfs_blocked(walls, start, end, maxx, maxy):
    # Directions for movement (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set()
    wall_set = set(walls)

    while queue:
        current_node = queue.popleft()

        if current_node in visited:
            continue
        visited.add(current_node)
        
        if current_node == end:
            return False

        # Explore neighbors
        for direction in directions:
            neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])
            if (
                0 <= neighbor[0] <= maxx and
                0 <= neighbor[1] <= maxy and
                neighbor not in wall_set and
                neighbor not in visited
            ):
                queue.append(neighbor)

    # If we exhaust the queue without reaching the end, the path is blocked
    return True

maxx = 70 
maxy = 70,
start= (0, 0)
end = (70, 70)
added_walls = []

# Add walls one by one and check the path
for i, wall in enumerate(walls):
    added_walls.append(wall)
    print(f"Checking wall {i+1}/{len(walls)}: {wall}")

    if bfs_blocked(added_walls, start, end, maxx, maxy):
        print(f"Path blocked after adding wall: {wall}")
        break
