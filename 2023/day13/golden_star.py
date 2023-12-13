def old_reflection(group):
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
                    return group[i]
            else:
                boolean = True
                for j in range(0,i+1):
                    if group[i-j] != group[i+1+j]:
                        boolean = False
                        break
                if boolean:
                    return group[i]
    
    columns = []
    for i, line in enumerate(group):
        for j, char in enumerate(line):
            if j >= len(columns):
                columns.append(char)
            else:
                columns[j] += char
    return old_reflection(columns)

def valid(line1, line2):
    x = line1.count("#")
    y = line2.count("#")

    for i in range(len(line1)):
        if line1[i] == "#" and line2[i] == "#":
            x -= 1
            y -= 1
    if x == 1 and y == 0 or x == 0 and y == 1:
        return True

def new_reflection(group,old):
    for i in range(len(group)):
        #ligne horizontale symétrie cote a cote
        if i+1 < len(group) and (group[i] == group[i+1] or valid(group[i],group[i+1])) :

            if group[i] in old and group[i+1] in old:
                continue

            if group[i] != group[i+1]:
                changed_sample = True
            else:
                changed_sample = False

            if len(group) - (i+1) <= i:
                boolean = True
                for j in range(len(group) - (i+1)):
                    if group[i-j] != group[i+1+j]:
                        if not changed_sample:
                            if valid(group[i-j],group[i+1+j]):
                                changed_sample = True
                            else:
                                boolean = False
                                break
                        else:
                            if j != 0:
                                boolean = False
                                break    
                if boolean:
                    return (i+1) * 100
            else:
                boolean = True
                for j in range(0,i+1):
                    if group[i-j] != group[i+1+j]:
                        if not changed_sample:
                            if valid(group[i-j],group[i+1+j]):
                                changed_sample = True
                            else:
                                boolean = False
                                break
                        else:
                            if j != 0:
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
    return int(new_reflection(columns,old) / 100)

with open("2023/day13/input.txt") as f:
    lines = f.readlines()
    group = []
    old_sym = []
    sum = 0
    for line in lines:
        if line == "\n":
            old_sym.append(old_reflection(group))
            sum += new_reflection(group,old_sym)
            group = []
            old_sym = []
        else:
            line = line.replace("\n", "")
            group.append(line)
    print(sum)