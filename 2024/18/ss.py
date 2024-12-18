import heapq

with open("2024/18/input.txt") as f:
    walls = set()
    lines = f.readlines()
    for i in range(1024):
        pos = lines[i].split(",")
        walls.add((int(pos[0]), int(pos[1])))

print(walls)

def dijkstra(walls, start, end, maxx, maxy):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(0, start)]
    distances = {start: 0}
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == end:
            return current_distance

        for direction in directions:
            neighbor = (current_node[0] + direction[0], current_node[1] + direction[1])
            if 0 <= neighbor[0] <= maxx and 0 <= neighbor[1] <= maxy and neighbor not in walls:
                distance = current_distance + 1
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

    return float('inf')


maxx = 70
maxy = 70
start = (0,0)
end = (70, 70) 
shortest_path_length = dijkstra(walls, start, end, maxx, maxy)
print(f"Shortest path length: {shortest_path_length}")


