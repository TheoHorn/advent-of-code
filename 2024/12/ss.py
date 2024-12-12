def spread(x, y, array):
    letter = array[y][x]
    to_visit = [(x, y)]
    region = set()

    while to_visit:
        cx, cy = to_visit.pop()
        if (cx, cy) in region:
            continue
        region.add((cx, cy))
        for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
            if 0 <= nx < len(array[0]) and 0 <= ny < len(array) and array[ny][nx] == letter and (nx, ny) not in region:
                to_visit.append((nx, ny))

    return region

def perimeter(region):
    perim = 0
    for x, y in region:
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if (nx, ny) not in region:
                perim += 1
    return perim



with open("2024/12/input.txt")as f:
    lines = f.readlines()
    array =  [f.strip() for f in lines]

seen = set()
count = 0
for y,line in enumerate(array):
    for x,letter in enumerate(line):
        if (x,y) not in seen:
            region = spread(x,y,array)
            area = len(region)
            perim = perimeter(region)
            count += area*perim
            seen.update(region)
print(count)