# Initialize variables
dug = {(0, 0)}  # Set of dug tiles, starting at (0, 0)
x, y = 0, 0  # Current position
directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}  # Direction mappings

# Read and process instructions from the input file
with open('2023/18/input.txt') as file:
    for line in file:
        direction, steps, hexa = line.split(" ")  # Split into direction and step count
        steps = int(steps)  # Convert step count to an integer
        for _ in range(steps):
            # Move in the specified direction and add the new position to the dug set
            dx, dy = directions[direction]
            x, y = x + dx, y + dy
            dug.add((x, y))

# Calculate the bounding box of the dug area
min_x = min(tile[0] for tile in dug)
max_x = max(tile[0] for tile in dug)
min_y = min(tile[1] for tile in dug)
max_y = max(tile[1] for tile in dug)

# Identify border tiles not part of the dug area
border_tiles = {
    (x, y) for y in range(min_y, max_y + 1) for x in [min_x, max_x] if (x, y) not in dug
} | {
    (x, y) for x in range(min_x, max_x + 1) for y in [min_y, max_y] if (x, y) not in dug
}

# Initialize sets for flood-fill
old_tiles = set()
new_tiles = border_tiles

# Perform flood-fill to find all external tiles
while new_tiles:
    next_tiles = set()
    for tile in new_tiles:
        for dx, dy in directions.values():
            neighbor = (tile[0] + dx, tile[1] + dy)
            if (
                min_x <= neighbor[0] <= max_x
                and min_y <= neighbor[1] <= max_y
                and neighbor not in dug
                and neighbor not in old_tiles
                and neighbor not in new_tiles
            ):
                next_tiles.add(neighbor)
    old_tiles.update(new_tiles)
    new_tiles = next_tiles

# Calculate and print the result
total_area = (max_x - min_x + 1) * (max_y - min_y + 1)
dug_area = len(old_tiles)
print(total_area - dug_area)
