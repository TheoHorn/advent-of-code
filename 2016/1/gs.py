with open("2016/1/input.txt") as f:
    ctn = f.read()
    values = ctn.split(', ')

x = 0
y = 0

direction = 0  # 0: North, 1: East, 2: South, 3: West
places = set()
places.add((x, y))
found = False
spot = None

for value in values:
    turn = value[0]
    steps = int(value[1:])
    
    if turn == 'R':
        direction = (direction + 1) % 4
    elif turn == 'L':
        direction = (direction - 1) % 4
    
    for _ in range(steps):
        if direction == 0:
            y += 1
        elif direction == 1:
            x += 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x -= 1
        
        if (x, y) in places and not found:
            spot = (x, y)
            found = True
        places.add((x, y))

distance = abs(spot[0]) + abs(spot[1])
print(f"Manhattan distance from first revisited spot: {distance}")
