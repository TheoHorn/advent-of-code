from collections import defaultdict

with open("2024/23/input.txt") as f:
    connections = [line.strip() for line in f]

graph = defaultdict(set)
for connection in connections:
    a, b = connection.split("-")
    graph[a].add(b)
    graph[b].add(a)

def find_largest_clique(graph):
    largest_clique = set()

    # Sort nodes by degree
    nodes = sorted(graph.keys(), key=lambda x: -len(graph[x]))

    for node in nodes:
        # Start a new potential clique
        current_clique = {node}
        candidates = graph[node].copy() 

        # Growing the clique
        while candidates:
            next_node = candidates.pop()
            if all(next_node in graph[clique_node] for clique_node in current_clique):
                current_clique.add(next_node)
                candidates.intersection_update(graph[next_node])

        if len(current_clique) > len(largest_clique):
            largest_clique = current_clique

    return largest_clique


largest_clique = find_largest_clique(graph)
largest_clique = sorted(largest_clique)
clique_name = ",".join(largest_clique)

print(f"Name of the largest LAN party: \n{clique_name}")
