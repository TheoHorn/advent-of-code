from itertools import combinations

with open("2015/17/input.txt") as f:
    lines = f.readlines()
    containers = [int(x.strip()) for x in lines]
    
    count = 0
    for i in range(len(containers)):
        for combination in combinations(containers,i+1):
            value = sum(combination)
            if value == 150:
                count += 1
    
    print(count)
            
    