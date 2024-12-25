def parse_visual(visual):
    # Split the visual into rows and calculate column heights.
    rows = visual.strip().split("\n")
    num_columns = len(rows[0])
    heights = [-1] * num_columns

    # Iterate through each column to determine height.
    for col in range(num_columns):
        for row in range(len(rows)):
            if rows[row][col] == "#":
                heights[col] += 1
    return heights


with open("2024/25/input.txt") as f:
    content = f.read().split("\n\n")

locks = []
keys = []
for ctn in content:
    if ctn.strip()[0] == "#": 
        locks.append(parse_visual(ctn))
    else:
        keys.append(parse_visual(ctn))

non_overlapping_pairs = set()
for lock in locks:
    for key in keys:
        if all(l + k < 6 for l, k in zip(lock, key)):
            non_overlapping_pairs.add((tuple(lock), tuple(key)))  

print(len(non_overlapping_pairs))
