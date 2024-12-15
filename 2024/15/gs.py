from collections import deque

# Works correctly in testing but has one unknown problem
# Read and parse the input
with open("2024/15/input.txt") as f:
    ctn = f.read()
    ctn = ctn.split("\n\n")
    box = ctn[0]
    moves = ctn[1]
    box = [list(line) for line in box.splitlines()]
    moves_queue = deque(char for line in moves.splitlines() for char in line)

# Transform tiles according to new rules (2x-wide tiles)
new_box = []
for row in box:
    new_row = []
    for char in row:
        if char == '#':
            new_row.append('##')
        elif char == 'O':
            new_row.append('[]')
        elif char == '.':
            new_row.append('..')
        elif char == '@':
            new_row.append('@.')
    new_box.append(''.join(new_row))

box = [list(row) for row in new_box]

# Locate the '@' robot
for i, row in enumerate(box):
    for j in range(0, len(row), 2):  # Step by 2 since tiles are now 2-wide
        if row[j:j+2] == ['@', '.']:
            position = (i, j)
            break

# Define movement directions
directions = {
    '^': (-1, 0),   # Up
    'v': (1, 0),    # Down
    '<': (0, -1),   # Left
    '>': (0, 1)     # Right
}

# Check bounds and if a tile is free
def is_within_bounds_and_empty(pos, box):
    x, y = pos
    return 0 <= x < len(box) and 0 <= y + 1 < len(box[0]) and box[x][y] == '.'
    

# Collect a chain of `[ ]` boxes in the direction of movement
def collect_chain(start_pos, direction, box):
    # Correct the new_position so it's pointing on '['
    if box[start_pos[0]][start_pos[1]] == ']':
        start_pos = (start_pos[0], start_pos[1] - 1)

    chain = []
    visited = set() 
    stack = [start_pos] 

    while stack:
        current = stack.pop()
        x, y = current

        if current in visited:
            continue

        visited.add(current)

        # Add the current position to the chain if it's a box
        if box[x][y] == '[' and box[x][y+1] == ']':
            chain.append((x, y))
            # Check the neighboring boxes in the direction of movement
            neighbors = []
            if direction == (-1, 0):  # Moving up
                neighbors = [(x - 1, y), (x - 1, y - 1), (x - 1, y + 1)]
            elif direction == (1, 0):  # Moving down
                neighbors = [(x + 1, y), (x + 1, y - 1), (x + 1, y + 1)]
            elif direction == (0, -1):  # Moving left
                neighbors = [(x, y - 2)]
            elif direction == (0, 1):  # Moving right
                neighbors = [(x, y + 2)]

            # Check if the neighbors are valid `[ ]` boxes and not already visited
            for neighbor in neighbors:
                nx, ny = neighbor
                if 0 <= nx < len(box) and 0 <= ny + 1 < len(box[0]):
                    if box[nx][ny] == '[' and box[nx][ny + 1] == ']' and neighbor not in visited:
                        # Check if the box can be pushed to be stacked
                        if direction == (1, 0) and nx + 1 < len(box) and box[nx + 1][ny] != '#' and box[nx + 1][ny + 1] != '#':
                            stack.append(neighbor)
                        elif direction == (-1, 0) and nx - 1 >= 0 and box[nx - 1][ny] != '#' and box[nx - 1][ny + 1] != '#':
                            stack.append(neighbor)
                        elif direction == (0, 1) and ny + 2 < len(box[0]) and box[nx][ny + 2] != '#':
                            stack.append(neighbor)
                        elif direction == (0, -1) and ny - 1 >= 0 and box[nx][ny - 1] != '#':
                            stack.append(neighbor)
                        else:
                            return None
    return chain

#with open("2024/15/output.txt", "w") as output_file:
#    for line in box:
#        output_file.write(''.join(line) + '\n')

# Process each move
while moves_queue:
    move = moves_queue.popleft()
    if move in directions:
        direction = directions[move]
        new_position = (position[0] + direction[0], position[1] + direction[1])

        # Move '@' to an empty space
        if is_within_bounds_and_empty(new_position, box):
            box[position[0]][position[1]] = '.'
            box[new_position[0]][new_position[1]] = '@'
            position = new_position

        # Handle pushing `[ ]` boxes
        elif box[new_position[0]][new_position[1]] == '[' or box[new_position[0]][new_position[1]] == ']':

            # Collect the chain of `[ ]` boxes
            chain = collect_chain(new_position, direction, box)
            if chain:
                # Determine the position after the chain
                
                if direction == (0, 1):
                    after_chain = (chain[-1][0] + direction[0], chain[-1][1] + 2)
                else:
                    after_chain = (chain[-1][0] + direction[0], chain[-1][1] + direction[1])
                # Check if there is space after the chain to push it
                if is_within_bounds_and_empty(after_chain, box):
                    # Move the chain of boxes
                    for pos in reversed(chain):
                        box[pos[0]][pos[1]] = '.'
                        box[pos[0]][pos[1]+1] = '.'
                        next_pos = (pos[0] + direction[0], pos[1] + direction[1])
                        box[next_pos[0]][next_pos[1]] = '['
                        box[next_pos[0]][next_pos[1]+1] = ']'

                    # Move the robot
                    box[position[0]][position[1]] = '.'
                    box[new_position[0]][new_position[1]] = '@'
                    position = new_position

    #Print the state of the box
    with open("2024/15/output.txt", "a") as output_file:
        output_file.write(f"Move = {move}\n")
        for line in box:
            output_file.write(''.join(line) + '\n')

# Calculate the score
score = 0
for x, row in enumerate(box):
    for y in range(0, len(row)):
        if row[y] =='[':
            score += x * 100 + y

print("Score:", score)
