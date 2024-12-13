import heapq
from collections import defaultdict
import re

# Parse input
with open("2015/19/input.txt") as f:
    lines = f.readlines()
    molecule = lines[-1].strip()
    rules = defaultdict(list)
    for line in lines[:-2]:
        elem = line.strip().split(" => ")
        rules[elem[1]].append(elem[0])  # Reverse rules for reverse BFS

# Reverse BFS with priority for shorter molecules
def reverse_bfs_with_priority(target, start, rules):
    queue = [(len(target), target, 0)]  # Priority queue: (length, molecule, steps)
    visited = set()
    
    while queue:
        _, current, steps = heapq.heappop(queue)
        if current == start:
            return steps
        if current in visited:
            continue
        visited.add(current)
        
        for key in rules:
            for value in rules[key]:
                for match in re.finditer(key, current):
                    new_molecule = current[:match.start()] + value + current[match.end():]
                    if new_molecule not in visited:
                        heapq.heappush(queue, (len(new_molecule), new_molecule, steps + 1))
    return -1

steps = reverse_bfs_with_priority(molecule, "e", rules)
print(f"Steps to reach the molecule: {steps}")
