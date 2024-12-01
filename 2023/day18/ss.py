def answer(data:str):
    lines = data.split("\n")

    for i in range(len(lines)):
        line = lines[i].split(" ")
        line[1] = int(line[1])
        lines[i] = line[0:2]
    
    size = 1400
    tab = [["."] * size for _ in range(size)]
    x = 1000
    y = 1000

    for line in lines:
        direction = line[0]
        length = int(line[1])
        old_x = x
        old_y = y
        if direction == "R":
            x += length
            for i in range(old_x, x + 1):
                tab[i][y] = "#"
        elif direction == "L":
            x -= length
            for i in range(old_x, x - 1, -1):
                tab[i][y] = "#"
        elif direction == "D":
            y -= length
            for i in range(old_y, y - 1, -1):
                tab[x][i] = "#"
        else:
            y += length
            for i in range(old_y, y + 1):
                tab[x][i] = "#"

    ##FILL

    for line in tab:
        started = False
        laststart = -2
        for i in range(len(line)):
            if line[i] == "#":
                if laststart != i-1:
                    started = not started
                else:
                    laststart = i
            else:
                if started: line[i] = "#"

    with open('2023/day18/answer.txt', 'w') as answer_file:
        for row in tab:
            answer_file.write("".join(row) + "\n")

    ## COUNT
    count = 0
    for line in tab:
        for x in line:
            if x == "#": count += 1
    
    return count

with open('2023/day18/input.txt', 'r') as f:
    print(answer(f.read()))


