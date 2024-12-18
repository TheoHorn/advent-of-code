with open("2016/2/input.txt") as f:
    rules = f.readlines()

MOVEMENTS = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

position = (2, 0)  # Starting at '5'
available_positions = {
    (0, 2), (1, 1), (1, 2), (1, 3),
    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
    (3, 1), (3, 2), (3, 3), (4, 2)
}
output = ""

keypad_value = {
    (0, 2): "1", (1, 1): "2", (1, 2): "3", (1, 3): "4",
    (2, 0): "5", (2, 1): "6", (2, 2): "7", (2, 3): "8", (2, 4): "9",
    (3, 1): "A", (3, 2): "B", (3, 3): "C", (4, 2): "D"
}

# Process each rule
for rule in rules:
    rule = rule.strip()
    for L in rule:
        if L in MOVEMENTS:
            move = MOVEMENTS[L]
            new_position = (position[0] + move[0], position[1] + move[1])
            if new_position in available_positions:
                position = new_position

    output += keypad_value[position]

print(f"Final output: {output}")