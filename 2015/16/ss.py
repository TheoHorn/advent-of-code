def finder(dico,thing,number):
    if dico[thing] != number: return False
    return True

with open("2015/16/ticker_tape.txt") as f:
    lines = f.readlines()
    infos = {}
    for line in lines:
        words = line.split(": ")
        infos[words[0]] = int(words[1])

with open("2015/16/input.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        words = lines[i].split(" ")
        val = words[2][:-1]
        number = int(words[3][:-1])

        if not finder(infos, val, number): continue

        val = words[4][:-1]
        number = int(words[5][:-1])
        if not finder(infos, val, number): continue

        val = words[6][:-1]
        number = int(words[7][:-1])
        if not finder(infos, val, number): continue

        print(i+1)
        break
