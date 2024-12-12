def spread(x, y, array):
    letter = array[y][x]
    to_visit = [(x, y)]
    surface = set()

    while to_visit:
        cx, cy = to_visit.pop()
        if (cx, cy) in surface:
            continue
        surface.add((cx, cy))
        for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
            if 0 <= nx < len(array[0]) and 0 <= ny < len(array) and array[ny][nx] == letter and (nx, ny) not in surface:
                to_visit.append((nx, ny))

    return surface


def sides(surface):
    s = 0
    for x, y in surface:
        # Outer
        s += (x-1, y) not in surface and (x, y-1) not in surface
        s += (x+1, y) not in surface and (x, y-1) not in surface
        s += (x-1, y) not in surface and (x, y+1) not in surface
        s += (x+1, y) not in surface and (x, y+1) not in surface
        # Inner
        s += (x-1, y) in surface and (x, y-1) in surface and (x-1, y-1) not in surface
        s += (x+1, y) in surface and (x, y-1) in surface and (x+1, y-1) not in surface
        s += (x-1, y) in surface and (x, y+1) in surface and (x-1, y+1) not in surface
        s += (x+1, y) in surface and (x, y+1) in surface and (x+1, y+1) not in surface
    return s


# Main Program Logic
with open("2024/12/input.txt") as f:
    lines = f.readlines()
    array = [line.strip() for line in lines]

seen = set()
count = 0
for y, line in enumerate(array):
    for x, letter in enumerate(line):
        if (x, y) not in seen:
            surface = spread(x, y, array)
            nb_sides = sides(surface)
            print(f"{letter} : {nb_sides}")
            area = len(surface)
            count += nb_sides * area
            seen.update(surface)

print(count)
