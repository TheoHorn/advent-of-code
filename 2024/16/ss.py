import heapq

with open("2024/16/input.txt") as f:
    lines = f.readlines()
    walls = set()
    start = None
    end = None

    # Parse the input file
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


directions = [(0,1), (1,0), (0,-1), (-1,0)]

# Dijkstra's algorithm implementation
def dijkstra(start, end):
    q = [(0, start, 0)]
    seen = set()
    while q:
        cost, pos, face = heapq.heappop(q)

        if (pos, face) in seen:  
            continue

        if pos == end: 
            return cost

        seen.add((pos,face))

        #forward
        next_cell = (pos[0]+directions[face][0], pos[1]+directions[face][1])
        if next_cell not in walls: 
            heapq.heappush(q,(cost+1, next_cell, face))

        # rotate
        heapq.heappush(q,(cost+1000, pos, (face - 1) % 4))
        heapq.heappush(q,(cost+1000, pos, (face + 1) % 4))


cost = dijkstra(start, end)
print("Part 1:", cost)
