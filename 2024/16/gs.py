import heapq
from collections import defaultdict

# Open the input file and read lines
with open("2024/16/input.txt") as f:
    lines = f.readlines()
    walls = set()
    start = None
    end = None

    # Parse the input file to identify walls, start, and end positions
    for x, line in enumerate(lines):
        for y, char in enumerate(line.strip()):
            if char == '#':
                walls.add((x, y))
            elif char == "S":
                start = (x, y)
            elif char == "E":
                end = (x, y)

# Validate that start and end positions were found
if start is None or end is None:
    raise ValueError("Start (S) or End (E) position is missing in the input file.")

# Define possible movement directions: right, down, left, up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Dijkstra's algorithm implementation to find the shortest path cost
def dijkstra(start, end):
    queue = [(0, start, 0)]  # (cost, position, direction_index)
    seen = set()

    while queue:
        cost, pos, face = heapq.heappop(queue)

        if (pos, face) in seen:
            continue

        if pos == end:
            return cost

        seen.add((pos, face))

        # Move forward
        next_cell = (pos[0] + directions[face][0], pos[1] + directions[face][1])
        if next_cell not in walls:
            heapq.heappush(queue, (cost + 1, next_cell, face))

        # Rotate left and right
        heapq.heappush(queue, (cost + 1000, pos, (face - 1) % 4))
        heapq.heappush(queue, (cost + 1000, pos, (face + 1) % 4))

# Calculate the cost using Dijkstra's algorithm
cost = dijkstra(start, end)

# Function to find all paths and count unique tiles visited
def find_all_paths(source, target, target_cost):
    best_costs = {}
    paths = defaultdict(set)

    queue = [(0, source, 0, None)]  # (cost, position, direction_index, previous_position)
    while queue:
        cost, pos, face, prev = heapq.heappop(queue)
        if cost > target_cost:
            break
        if (pos, face) in best_costs:
            if cost == best_costs[(pos, face)]:
                paths[(pos, face)].add(prev)
            continue

        best_costs[(pos, face)] = cost
        paths[(pos, face)].add(prev)

        prev = (pos, face)

        # Move forward
        next_cell = (pos[0] + directions[face][0], pos[1] + directions[face][1])
        if next_cell not in walls:
            heapq.heappush(queue, (cost + 1, next_cell, face, prev))

        # Rotate left and right
        heapq.heappush(queue, (cost + 1000, pos, (face - 1) % 4, prev))
        heapq.heappush(queue, (cost + 1000, pos, (face + 1) % 4, prev))

    routes, tiles = set(), set()

    def back_finder(current_position):
        # Recursive function to find through the paths and collect routes and tiles
        if current_position and current_position not in routes:
            routes.add(current_position)
            tiles.add(current_position[0])
            for next_position in paths[current_position]:
                back_finder(next_position)

    # Start walking from the target position for all possible facing directions
    for face in range(4):
        back_finder((target, face))

    return len(tiles)

# Print the result of Part 2
print(find_all_paths(start, end, cost))
