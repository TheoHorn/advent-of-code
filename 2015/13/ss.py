# Description: Solution for Day 13 in Advent of Code 2015
with open("2015/13/input.txt") as f:
    lines = f.readlines()
    names = []
    for line in lines:
        words = line.split(" ")
        name = words[0]
        if name not in names:
            names.append(name)

    happiness = {}
    for name in names:
        happiness[name] = {}
        for name2 in names:
            if name != name2:
                happiness[name][name2] = 0
    
    for line in lines:
        words = line.split(" ")
        name = words[0]
        if words[-1][-1] == "\n":
            name2 = words[-1][:-2]
        else:
            name2 = words[-1][:-1]
        happiness[name][name2] = int(words[3]) if words[2] == "gain" else -int(words[3])

    names.append("Me")
    happiness["Me"] = {}
    for name in names:
        happiness["Me"][name] = 0
        happiness[name]["Me"] = 0

    from itertools import permutations
    max_happiness = 0
    print(happiness)
    for perm in permutations(names):
        print(perm)
        happiness_sum = 0
        for i in range(len(perm)):
            happiness_sum += happiness[perm[i]][perm[(i+1)%len(perm)]] + happiness[perm[(i+1)%len(perm)]][perm[i]]
        max_happiness = max(max_happiness, happiness_sum)

    print(max_happiness)

    

