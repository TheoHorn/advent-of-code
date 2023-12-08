dico = {}

with open ('2023/day8/input.txt') as f:
    lines = f.read().splitlines()
    direction = lines[0]
    for i in range(2,len(lines)):
        line = lines[i].split(' = ')
        fin_line = line[1].replace('(','').replace(')','').replace(' ','').split(',')
        dico[line[0]] = (fin_line[0],fin_line[1])
    
    current_position = 'AAA'
    i = 0
    nb_steps = 0 
    while current_position != 'ZZZ':
        if i == len(direction):
            i = 0
        if direction[i] == 'L':
            current_position = dico[current_position][0]
            nb_steps += 1
        elif direction[i] == 'R':
            current_position = dico[current_position][1]
            nb_steps += 1
        i += 1
    print(nb_steps)
