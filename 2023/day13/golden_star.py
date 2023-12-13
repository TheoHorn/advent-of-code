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
                    return "ligne"+ str(i+1)
            else:
                boolean = True
                for j in range(0,i+1):
                    if group[i-j] != group[i+1+j]:
                        boolean = False
                        break
                if boolean:
                    return "ligne"+ str(i+1)
    
    columns = []
    for i, line in enumerate(group):
        for j, char in enumerate(line):
            if j >= len(columns):
                columns.append(char)
            else:
                columns[j] += char
    return old_reflection(columns).replace("ligne", "colonne")

def valid(line1, line2):
    x = line1.count("#")
    y = line2.count("#")

    if x - 1 > 0 and x-1 == y or x +1 < len(line1) and x+1 == y:
        return True

def new_reflection(group):
    for i in range(len(group)):
        #ligne horizontale symétrie cote a cote
        if i+1 < len(group) and valid(group[i], group[i+1]):

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
    return int(new_reflection(columns) / 100)

with open("2023/day13/input.txt") as f:
    lines = f.readlines()
    group = []
    old_sym = []
    for line in lines:
        if line == "\n":
            old_sym.append(old_reflection(group))
            sum += new_reflection(group)
            group = []
        else:
            line = line.replace("\n", "")
            group.append(line)
    print(sum)