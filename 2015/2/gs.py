f = open("input.txt", "r")
total = 0
i = 0
line = f.readline()
while line:
    line = line.split("x")
    l = int(line[0])
    w = int(line[1])
    h = int(line[2])
    total += w*h*l
    if l < w and l < h:
        total += 2*l
        if w < h:
            total += 2*w
        else:
            total += 2*h
    elif w < h:
        total += 2*w
        if l < h:
            total += 2*l
        else:
            total += 2*h
    else:
        total += 2*h
        if l < w:
            total += 2*l
        else:
            total += 2*w
    line = f.readline()


print(total)