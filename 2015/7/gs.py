from operation import AND, OR, LSHIFT, RSHIFT, NOT
dico = {}
while 'a' not in dico:
    with open('2015/day7/input.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
            dico['b'] = 16076
            line = line.split(' ')
            if len(line) == 3:
                if line[0].isdigit():
                    dico[line[2]] = line[0]
                    print(line[2], ":", line[0], "=", dico[line[2]])
                else:
                    if line[0] in dico:
                        dico[line[2]] = dico[line[0]]
                        print(line[2], ":", line[0], "=", dico[line[2]])
            else:
                if line[0] in dico and line[2] in dico:
                    if 'OR' in line:
                        dico[line[4]] = OR(dico[line[0]], dico[line[2]])
                        print(line[4], ":", line[0], "OR", line[2], "=", dico[line[4]])
                if line[1] in dico:
                    if 'NOT' in line:
                        dico[line[3]] = NOT(dico[line[1]])
                        print(line[3], ":", "NOT", line[1], "=", dico[line[3]])
                if line[0] in dico:
                    if 'LSHIFT' in line:
                        dico[line[4]] = LSHIFT(dico[line[0]], line[2])
                        print(line[4], ":", line[0], "LSHIFT", line[2], "=", dico[line[4]])
                    if 'RSHIFT' in line:
                        dico[line[4]] = RSHIFT(dico[line[0]], line[2])
                        print(line[4], ":", line[0], "RSHIFT", line[2], "=", dico[line[4]])
                if line[2] in dico:
                    if 'AND' in line:
                        if line[0] == '1':
                            dico[line[4]] = AND('1', dico[line[2]])
                            print(line[4], ": 1 ", "AND", line[2], "=", dico[line[4]])
                        elif line[0] in dico:
                            dico[line[4]] = AND(dico[line[0]], dico[line[2]])
                            print(line[4], ":", line[0], "AND", line[2], "=", dico[line[4]])
                
print(dico['a'])