import re

with open("2015/25/input.txt") as f:
    ctn = f.read()
    numbers = re.findall(r"\d+", ctn)

row = int(numbers[0])
col = int(numbers[1])

# Initialize the first code
current_code = 20151125

def next_code(code):
    return (code * 252533) % 33554393

# Find target coordinates in diagonal traversal
i, j = 1, 1  # Starting position (1-based indexing)

target_row, target_col = row, col

while (i, j) != (target_row, target_col):
    current_code = next_code(current_code)
    if i == 1:
        i = j + 1
        j = 1
    else:
        i -= 1
        j += 1

print(current_code)
