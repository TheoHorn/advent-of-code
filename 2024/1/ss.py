with open("2024/day1/input.txt") as f:
    lines = f.readlines()
    l1 = []
    l2= []
    for line in lines:
        values = line.split("   ")
        l1.append(values[0])
        l2.append(values[1])

    l1.sort()
    l2.sort()
    diff = 0
    for i in range(len(l1)):
        diff += abs(int(l1[i])-int(l2[i]))
    
    print(diff)