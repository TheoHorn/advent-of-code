with open("2016/1/input.txt") as f:
    ctn = f.read()
    values = ctn.split(', ')

x = 0
y = 0

direction = 0  # 0: North, 1: East, 2: South, 3: West
for value in values:
    turn = value[0]
    steps = int(value[1:])
    
    if turn == 'R':
        direction = (direction + 1) % 4
    elif turn == 'L':
        direction = (direction - 1) % 4
    
    if direction == 0:
        y += steps
    elif direction == 1:
        x += steps
    elif direction == 2:
        y -= steps
    elif direction == 3:
        x -= steps

distance = abs(x) + abs(y)
print(f"Manhattan distance: {distance}")