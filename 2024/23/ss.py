from collections import defaultdict

with open("2024/23/input.txt") as f:
    connections = [line.strip() for line in f]

graph = defaultdict(set)
for connection in connections:
    a, b = connection.split("-")
    graph[a].add(b)
    graph[b].add(a)

def find_triangles(graph):
    triangles = set()
    for node in graph:
        for neighbor in graph[node]:
            common_neighbors = graph[node].intersection(graph[neighbor])
            for common in common_neighbors:
                triangle = tuple(sorted([node, neighbor, common]))
                triangles.add(triangle)
    return triangles

# Find all triangles
triangles = find_triangles(graph)

def starts_with_t(triangle):
    return any(computer.startswith('t') for computer in triangle)

triangles_with_t = [triangle for triangle in triangles if starts_with_t(triangle)]
print("Triangles with 't':", triangles_with_t)
print(f"Triangles with at least one 't': \n{len(triangles_with_t)}")
