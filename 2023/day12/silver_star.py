def configurations(config, group):

    
    if (len(group) == 0):
        a = 0
        for c in config:
            if c == 1:
                a += 1
        if a == 0:
            return 1
        else:
            return 0
        
    if sum(group) > len(config):
        return 0
    
    if config[0] == 0:
        a = configurations(config[1:], group)
        return a

    no1, no2 = 0, 0
    if config[0] == 2:
        no2 = configurations(config[1:], group)

    
    bool = True
    for c in config[:group[0]]:
        if c == 0:
            bool = False

    bool2 = False
    if len(config) > group[0]:
        if config[group[0]] == 1:
            bool2 = True
    else:
        bool2 = False
        
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

        
