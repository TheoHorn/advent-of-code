# Load the initial configuration from the input file
with open("2015/18/input.txt") as f:
    ctn = [list(line.strip()) for line in f.readlines()]

# Ensure corners are always "on"
for x, y in [(0, 0), (0, len(ctn[0]) - 1), (len(ctn) - 1, 0), (len(ctn) - 1, len(ctn[0]) - 1)]:
    ctn[x][y] = "#"

iterations = 100
current_array = ctn

# Run the simulation for the specified number of iterations
for _ in range(iterations):
    # Create the next state array
    next_array = [['.' for _ in range(len(current_array[0]))] for _ in range(len(current_array))]
    
    for x, line in enumerate(current_array):
        for y, val in enumerate(line):
            neighbors_on = 0
            
            # Count the number of neighboring cells that are "on" (#)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(current_array) and 0 <= ny < len(current_array[0]):
                        if current_array[nx][ny] == "#":
                            neighbors_on += 1

            # Apply the rules of the Game of Life
            if val == "#":
                # A light that is on stays on if it has 2 or 3 neighbors that are on
                next_array[x][y] = "#" if neighbors_on in [2, 3] else "."
            else:
                # A light that is off turns on if it has exactly 3 neighbors that are on
                next_array[x][y] = "#" if neighbors_on == 3 else "."

    # Ensure corners are always "on"
    for x, y in [(0, 0), (0, len(next_array[0]) - 1), (len(next_array) - 1, 0), (len(next_array) - 1, len(next_array[0]) - 1)]:
        next_array[x][y] = "#"

    # Update the current array to the next state
    current_array = next_array

# Count the number of lights that are on after the last iteration
count = sum(line.count("#") for line in current_array)

print(count)
