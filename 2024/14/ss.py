import re

robots = []

with open("2024/14/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        digits = re.findall(r'-?\d+', line)
        digits = list(map(int, digits))
        robots.append(digits)

# Simulation parameters
time_to_simulate = 100
max_x = 100
max_y = 102
quadrants = [0] * 4  # top left, top right, bottom right, bottom left

for robot in robots:
    x = robot[0]
    y = robot[1]
    vel_x = robot[2]
    vel_y = robot[3]

    for _ in range(time_to_simulate):
        # Update position and handle teleportation while conserving velocity
        x = (x + vel_x) % (max_x + 1)
        y = (y + vel_y) % (max_y + 1)

    # Determine the quadrant, excluding the middle ground
    if x == max_x / 2 or y == max_y / 2:  # Middle ground check
        continue
    elif x < max_x / 2 and y < max_y / 2:
        quadrants[0] += 1  # Top left
    elif x > max_x / 2 and y < max_y / 2:
        quadrants[1] += 1  # Top right
    elif x > max_x / 2 and y > max_y / 2:
        quadrants[2] += 1  # Bottom right
    else:
        quadrants[3] += 1  # Bottom left

# Calculate the result
result = 1
for quadrant in quadrants:
    result *= quadrant

print(result)
