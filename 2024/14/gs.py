import re
from PIL import Image
import numpy as np

robots = []

with open("2024/14/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        digits = re.findall(r'-?\d+', line)
        digits = list(map(int, digits))
        robots.append(digits)

# Simulation parameters
time_to_simulate = 200000
max_x = 100
max_y = 102
threshold_variance = 733 

for t in range(time_to_simulate):
    grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    positions_x = []
    positions_y = []

    for robot in robots:
        x, y, vel_x, vel_y = robot

        x = (x + vel_x) % (max_x + 1)
        y = (y + vel_y) % (max_y + 1)

        robot[0], robot[1] = x, y

        grid[y][x] += 1
        positions_x.append(x)
        positions_y.append(y)

    # Calculate variances
    variance_x = np.var(positions_x)
    variance_y = np.var(positions_y)
    total_variance = variance_x + variance_y

    # Save the image if variance is below the threshold
    if total_variance < threshold_variance:
        print(f"Pattern detected at step {t} with variance {total_variance}")

        img = Image.new('RGB', (max_x + 1, max_y + 1), color='white')
        pixels = img.load()

        for y in range(max_y + 1):
            for x in range(max_x + 1):
                if grid[y][x] > 0:
                    intensity = 0
                    pixels[x, y] = (intensity, intensity, intensity)

        img.save(f"2024/14/output/compact_pattern_at_t{t}.png")
