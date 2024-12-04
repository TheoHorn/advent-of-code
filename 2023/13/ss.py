def reflection(group):
    for i in range(len(group)):
        #ligne horizontale symétrie cote a cote
        if i+1 < len(group) and group[i] == group[i+1]:

            if len(group) - (i+1) <= i:
                boolean = True
                for j in range(len(group) - (i+1)):
                    if group[i-j] != group[i+1+j]:
                        boolean = False
                        break                
                if boolean:
                    return (i+1) * 100
            else:
                boolean = True
                for j in range(0,i+1):
                    if group[i-j] != group[i+1+j]:
                        boolean = False
                        break
                if boolean:
                    return (i+1) * 100
    
    columns = []
    for i, line in enumerate(group):
        for j, char in enumerate(line):
            if j >= len(columns):
                columns.append(char)
            else:
                columns[j] += char
    return int(reflection(columns) / 100)


with open("2023/day13/input.txt") as f:
    lines = f.readlines()
    group = []
    sum = 0
    for line in lines:
        if line == "\n":
            sum += reflection(group)
            print(sum, group)
            group = []
        else:
            line = line.replace("\n", "")
            group.append(line)
    print(sum)