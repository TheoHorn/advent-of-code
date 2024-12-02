def configurations(config, group):

    #si on a fini de tester les groupes
    if (len(group) == 0):
        a = 0
        #si il reste des # -> nok
        for c in config:
            if c == 1:
                a += 1
        if a == 0:
            return 1
        else:
            return 0
    
    #si il reste pas assez de place pour le groupe
    if sum(group) > len(config):
        return 0
    
    #si on est sur un point, on passe au suivant
    if config[0] == 0:
        a = configurations(config[1:], group)
        return a

    no1, no2 = 0, 0

    #si on est sur un ?, on teste notre groupe sur la suite 
    if config[0] == 2:
        no2 = configurations(config[1:], group)

    
    #si on trouve un 0 après dans les group[0]-nième valeur -> nok
    bool = True
    for c in config[:group[0]]:
        if c == 0:
            bool = False

    #si notre groupe est bon -> ok
    bool2 = False
    if len(config) > group[0]:
        if config[group[0]] == 1:
            bool2 = True
    else:
        bool2 = False
        
    #si 1 et 2 -> ok, on teste la suite à la prochaine valeur et avec le groupe suivant
    if bool and bool2 != 1:
        no1 = configurations(config[(group[0] + 1):], group[1:])
     

    return no1 + no2

with open("2023/day12/input.txt") as f:
    total = 0
    for line in f:
        val,l = line.strip().split(' ')

        val_to_int = {'.': 0, '#': 1, '?': 2}
        val = [val_to_int[x] for x in val]

        l = [int(x) for x in l.split(',')]

        arr = configurations(tuple(val), tuple(l))
        total += arr

print(total)

        
