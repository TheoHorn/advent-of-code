with open("2024/19/input.txt") as f:
    ctn = f.read().split("\n\n")
    patterns = set()
    for pattern in ctn[0].split(", "):
        patterns.add(pattern)
    
    towels = []
    for line in ctn[1].splitlines():
        towels.append(line)




def can_be_constructed(target, patterns_set):
    if not target:
        return True  

    for pattern in patterns_set:
        if target.startswith(pattern):
            # Recursively check the rest of the target
            if can_be_constructed(target[len(pattern):], patterns_set):
                return True
    return False

# Sort patterns by length
patterns = sorted(patterns, key=len)

# Keep primary patterns
primary_patterns = []
patterns_set = set()

for pattern in patterns:
    if not can_be_constructed(pattern, patterns_set):
        primary_patterns.append(pattern)
        patterns_set.add(pattern)

print(primary_patterns)
count = 0
total_towels = len(towels)
for i, towel in enumerate(towels):
    if can_be_constructed(towel, primary_patterns):
        count += 1
        print(f"Valid : {count}")
    else:
        print("Impossible")
    print(f"Progress: {((i + 1) / total_towels) * 100:.2f}%")
print(count)