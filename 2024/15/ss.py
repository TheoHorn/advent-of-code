from collections import deque

with open("2024/15/input.txt") as f:
    ctn = f.read()
    ctn = ctn.split("\n\n")
    box = ctn[0]
    moves = ctn[1]
    box = [list(line) for line in box.splitlines()]
    moves_queue = deque(char for line in moves.splitlines() for char in line)

# Find @
for i, row in enumerate(box):
    for j, char in enumerate(row):
        if char == '@':
            position = (i, j)
            break

# Do the movement to @
directions = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

# Helper to validate if a position is within bounds and empty
def is_within_bounds_and_empty(pos, box):
    return 0 <= pos[0] < len(box) and 0 <= pos[1] < len(box[0]) and box[pos[0]][pos[1]] == '.'

# Process each move
while moves_queue:
    move = moves_queue.popleft()
    if move in directions:
        direction = directions[move]
        new_position = (position[0] + direction[0], position[1] + direction[1])
        
        if 0 <= new_position[0] < len(box) and 0 <= new_position[1] < len(box[0]):
            if box[new_position[0]][new_position[1]] == '.':
                # Move @ to new position
                box[position[0]][position[1]] = '.'
                position = new_position
                box[position[0]][position[1]] = '@'

            elif box[new_position[0]][new_position[1]] == 'O':
                # Handle 'O'
                chain = []
                current = new_position
                while 0 <= current[0] < len(box) and 0 <= current[1] < len(box[0]) and box[current[0]][current[1]] == 'O':
                    chain.append(current)
                    current = (current[0] + direction[0], current[1] + direction[1])
                
                # Check if the position after the last 'O' is free
                if is_within_bounds_and_empty(current, box):
                    # Move all 'O's in the chain and update the position of '@'
                    for i in range(len(chain) - 1, -1, -1):  # Start from the end of the chain
                        box[chain[i][0]][chain[i][1]] = '.'
                        next_pos = (chain[i][0] + direction[0], chain[i][1] + direction[1])
                        box[next_pos[0]][next_pos[1]] = 'O'
                    # Move @
                    box[position[0]][position[1]] = '.'
                    box[new_position[0]][new_position[1]] = '@'
                    position = new_position

# Find the score 
score = 0
for x, row in enumerate(box):
    for y, char in enumerate(row):
        if char == 'O':
            score += x * 100 + y

print("Score:", score)