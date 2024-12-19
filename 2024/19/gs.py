from functools import lru_cache

with open("2024/19/input.txt") as f:
    ctn = f.read().split("\n\n")
    patterns = set()
    for pattern in ctn[0].split(", "):
        patterns.add(pattern)
    
    towels = []
    for line in ctn[1].splitlines():
        towels.append(line)

patterns = sorted(patterns, key=len)

@lru_cache(None)  
def count_constructions(target):
    if not target:
        return 1 

    count = 0
    for pattern in patterns:
        if target.startswith(pattern):
            count += count_constructions(target[len(pattern):])
    return count


count = 0
total_towels = len(towels)
for i, towel in enumerate(towels):
    count += count_constructions(towel)
    print(f"Progress: {((i + 1) / total_towels) * 100:.2f}%")
print(count)
