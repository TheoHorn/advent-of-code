with open("2023/day6/input.txt") as f:
    data = f.read().splitlines()
    time =[]
    distance = []
    for i in range(len(data)):
        line = data[i].split(" ")
        for j in range(1,len(line)):
            if line[j] == " " or line[j] == "":
                continue
            else:
                if i ==0 :
                    time.append(int(line[j]))
                else:
                    distance.append(int(line[j]))
    factor = 1
    for t in range(len(time)) :
        somme = 0
        speed = 0
        dist = 0
        for i in range(0,time[t]):
            speed = i
            
            dist = (time[t]-i) * speed
            if dist > distance[t]:
                print("dist",dist,">",distance[t])
                somme = somme + 1
        factor = somme * factor
    print(factor)
            
                

            