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
                    time.append(line[j])
                else:
                    distance.append(line[j])
    time_total = ""
    for t in time :
        time_total = time_total + t
    time_total = int(time_total)
    distance_total = ""
    for d in distance :
        distance_total = distance_total + d
    distance_total = int(distance_total)
    factor = 1
    somme = 0
    speed = 0
    dist = 0
    for i in range(0,time_total):
        speed = i
        
        dist = (time_total-i) * speed
        if dist > distance_total:
            somme = somme + 1
    factor = somme * factor
    print(factor)
            
                

            