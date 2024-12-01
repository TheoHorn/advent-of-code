with open("2024/day1/input.txt") as f:
    lines = f.readlines()
    l1 = []
    l2= []
    for line in lines:
        values = line.split("   ")
        l1.append(int(values[0]))
        l2.append(int(values[1]))

    l1.sort()
    l2.sort()
    diff = 0
    
    for value in l1:
        nb = 0
        for apparition in l2:
            if apparition == value : nb +=1
        diff += nb * value
    
    print(diff)