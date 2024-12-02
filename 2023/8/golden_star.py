
import math


def find_path(cp, nb_steps,direction,i):
    current_position = cp
    bool = True
    while bool or (current_position != cp and not current_position.endswith('Z')):
        bool = False
        if i == len(direction):
            i = 0
        if direction[i] == 'L':
            new_current_position = dico[current_position][0]
            nb_steps += 1
        elif direction[i] == 'R':
            new_current_position = dico[current_position][1]
            nb_steps += 1
        if new_current_position == current_position:
            break
        current_position = new_current_position
        i += 1
    return nb_steps, current_position , i



dico = {}
start = []
with open ('2023/day8/input.txt') as f:
    lines = f.read().splitlines()
    direction = lines[0]
    for i in range(2,len(lines)):
        line = lines[i].split(' = ')
        fin_line = line[1].replace('(','').replace(')','').replace(' ','').split(',')
        if line[0].endswith('A'):
            start.append(line[0])
        dico[line[0]] = (fin_line[0],fin_line[1])
    
    new_dico = []
    for a in start:
        current_position = a
        nb_steps = 0
        i = 0
        nb_steps, current_position, i = find_path(current_position, nb_steps,direction,i)
        new_dico.append(nb_steps)


print(math.lcm(*new_dico))
print(new_dico)