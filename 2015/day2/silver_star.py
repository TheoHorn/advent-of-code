f = open("input.txt", "r")


total = 0
i = 0
line = " "
while(line != ''):
    line = f.readline()
    line = line.split("x")
    l = int(line[0])
    w = int(line[1])
    h = int(line[2])
    total += 2*l*w + 2*w*h + 2*h*l
    if l*w < w*h and l*w < h*l:
        total += l*w
    elif w*h < h*l:
        total += w*h
    else:
        total += h*l
    i += 1
    print(i)
    print(total)

print(total)