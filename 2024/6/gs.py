TURN = {( 0, -1): ( 1,  0),    # Up -> Right
        ( 1,  0): ( 0,  1),    # Right -> Down
        ( 0,  1): (-1,  0),    # Down -> Left
        (-1,  0): ( 0, -1),    # Left -> Up
       }

def part1(filename):
    with open(filename, 'r') as fp:
        lines = [line.strip() for line in fp.readlines()]

    blocks = set()
    for y, line in enumerate(lines):
        for x, space in enumerate(line):
            if space == '#':
                blocks.add((x, y))
            elif space == '^':
                pos = (x, y)

    visited = set()
    direction = (0, -1)
    while (0 <= pos[0] < len(lines)) and (0 <= pos[1] < len(lines[0])):
        visited.add(pos)
        step = pos[0] + direction[0], pos[1] + direction[1]
        if step in blocks:
            direction = TURN[direction]
        else:
            pos = step

    answer = len(visited)
    return answer, visited

def part2(filename, path):
    with open(filename, 'r') as fp:
        lines = [line.strip() for line in fp.readlines()]

    blocks = set()
    for y, line in enumerate(lines):
        for x, space in enumerate(line):
            if space == '#':
                blocks.add((x, y))
            elif space == '^':
                pos = (x, y)

    start = pos
    answer = 0
    for x, y in path:
        visited = set()
        pos = start
        direction = (0, -1)
        loop = False
        while (0 <= pos[0] < len(lines)) and (0 <= pos[1] < len(lines[0])) and (not loop):
            state = (pos, direction)
            if state in visited:
                loop = True
                continue
            
            visited.add(state)
            step = pos[0] + direction[0], pos[1] + direction[1]
            if (step in blocks) or (step == (x, y)):
                direction = TURN[direction]
            else:
                pos = step
        answer += loop

    print(answer)

ans, path = part1("2024/6/input.txt")
print(ans)
part2("2024/6/input.txt", path)