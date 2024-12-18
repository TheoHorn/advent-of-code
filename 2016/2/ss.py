with open("2016/2/input.txt") as f:
    rules = f.readlines()

MOVEMENTS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

position = (1,1)
output=""
for rule in rules:
    for L in rule:
        if L in MOVEMENTS:
            move = MOVEMENTS[L]
            new_position = (position[0] + move[0], position[1] + move[1])
            if 0 <= new_position[0] <= 2 and 0 <= new_position[1] <= 2:
                position = new_position
    output += str(position[0] + position[1] * 3 + 1)
print(output)