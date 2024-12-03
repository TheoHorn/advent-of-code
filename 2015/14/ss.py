with open("2015/14/input.txt") as f:
    lines = f.readlines()
    reindeers = {}
    for line in lines:
        words = line.split(" ")
        reindeers[words[0]] = {
            "speed": int(words[3]),
            "fly_time": int(words[6]),
            "rest_time": int(words[13]),
        }
    
    def distance(speed,time_speed,rest,time):
        q = time // (time_speed+rest)
        r = time % (time_speed+rest)
        value = q*speed*time_speed
        if r > time_speed:
            value += time_speed*speed
        else:
            value += r*speed
        return value

    time_to_fly = 2503
    maxi = 0
    for r in reindeers:
        maxi = max(distance(reindeers[r]["speed"],reindeers[r]["fly_time"],reindeers[r]["rest_time"],time_to_fly),maxi)
    #2660
    print(maxi)

                






