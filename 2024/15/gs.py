from collections import deque
import os

def read_and_parse_input(input_file):
    """Reads and parses the input file into a box and moves queue."""
    with open(input_file) as f:
        ctn = f.read().split("\n\n")
        box = [list(line) for line in ctn[0].splitlines()]
        moves_queue = deque(char for line in ctn[1].splitlines() for char in line)

    return box, moves_queue

def transform_box(box):
    """Transforms the box according to new rules (2x-wide tiles)."""
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
    return [list(row) for row in new_box]

def locate_robot(box):
    """Locates the initial position of the '@' robot."""
    for i, row in enumerate(box):
        for j in range(0, len(row) - 1, 2):  # Step by 2 since tiles are now 2-wide
            if row[j:j + 2] == ['@', '.']:
                return (i, j)
    return None

def is_within_bounds_and_empty_robot(pos, box):
    """Checks if the position is within bounds and empty for the robot."""
    x, y = pos
    return 0 <= x < len(box) and 0 <= y + 1 < len(box[0]) and box[x][y] == '.'

def collect_chain(start_pos, direction, box):
    """Collects a chain of `[ ]` boxes in the direction of movement."""
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

        if box[x][y] == '[' and box[x][y + 1] == ']':
            chain.append((x, y))

            # Check that if it is going up or down there is no "#" that blocks one part of the current box and it is within the bounds
            if direction == (-1, 0):  # Moving up
                if (x - 1 >= 0 and (box[x-1][y] == '#' or box[x-1][y + 1] == '#')):
                    return None
            elif direction == (1, 0):  # Moving down
                if (x + 1 < len(box) and (box[x+1][y] == '#' or box[x+1][y + 1] == '#')):
                    return None
            elif direction == (0, -1):  # Moving left
                if (y - 1 >= 0 and box[x][y - 1] == '#'):
                    return None
            elif direction == (0, 1):  # Moving right
                if (y + 2 < len(box[0]) and box[x][y + 2] == '#'):
                    return None
            
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

            for neighbor in neighbors:
                nx,ny = neighbor
                if (0 <= nx < len(box) and 0 <= ny + 1 < len(box[0]) and
                    box[nx][ny] == '[' and box[nx][ny + 1] == ']' and
                    (nx, ny) not in visited):
                    stack.append((nx, ny))

    if len(chain) == 0:
        return None
    else:
        return chain

def move_robot_and_boxes(move, position, box, directions):
    """Handles the movement of the robot and any `[ ]` boxes."""
    direction = directions[move]
    new_position = (position[0] + direction[0], position[1] + direction[1])
    chain = None
    if is_within_bounds_and_empty_robot(new_position, box):
        # Move the robot
        box[position[0]][position[1]] = '.'
        box[new_position[0]][new_position[1]] = '@'
        return box, new_position,chain

    elif box[new_position[0]][new_position[1]] == '[' or box[new_position[0]][new_position[1]]== ']':
        chain = collect_chain(new_position, direction, box)
        if chain:
            # Move the chain
            if direction == (0, -1):  # Moving left
                chain = sorted(chain, key=lambda x: x[1])
            elif direction == (0, 1):  # Moving right
                chain = sorted(chain, key=lambda x: x[1], reverse=True)
            elif direction == (-1, 0):  # Moving up
                chain = sorted(chain, key=lambda x: x[0])
            elif direction == (1, 0):  # Moving down
                chain = sorted(chain, key=lambda x: x[0], reverse=True)

            for pos in chain:
                box[pos[0]][pos[1]] = '.'
                box[pos[0]][pos[1] + 1] = '.'
                next_pos = (pos[0] + direction[0], pos[1] + direction[1])
                box[next_pos[0]][next_pos[1]] = '['
                box[next_pos[0]][next_pos[1] + 1] = ']'

            # Move the robot
            box[position[0]][position[1]] = '.'
            box[new_position[0]][new_position[1]] = '@'
            return box, new_position,chain

    return box, position, chain

def write_box_to_file(box, output_file, move=None, chain= None):
    """Writes the current state of the box to the output file."""
    with open(output_file, "a") as output:
        #if chain and len(chain) > 2:
            if move:
                output.write(f"Move = {move}\n")
            for line in box:
                output.write(''.join(line) + '\n')

def calculate_score(box):
    """Calculates the final score based on the box's state."""
    score = 0
    for x, row in enumerate(box):
        for y in range(len(row)):
            if row[y] == '[':
                score += x * 100 + y
    return score

def main():
    input_file = "2024/15/input.txt"
    output_file = "2024/15/output.txt"
    if os.path.exists(output_file):
        os.remove(output_file)

    # Directions mapping
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    # Read and parse input
    box, moves_queue = read_and_parse_input(input_file)
    # Transform box
    box = transform_box(box)

    # Locate robot
    position = locate_robot(box)

    # Write initial box state
    write_box_to_file(box, output_file)

    # Process moves
    while moves_queue:
        move = moves_queue.popleft()
        if move in directions:
            box, position,chain = move_robot_and_boxes(move, position, box, directions)
            write_box_to_file(box, output_file, move,chain)

    # Calculate and print the score
    score = calculate_score(box)
    print("Score:", score)

if __name__ == "__main__":
    main()
