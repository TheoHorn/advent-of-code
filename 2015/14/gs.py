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
    scores = {}
    for reindeer in reindeers:
        scores[reindeer] = 0

    for i in range(1,time_to_fly):
        values = {}
        for r in reindeers:
            values[r]= distance(reindeers[r]["speed"],reindeers[r]["fly_time"],reindeers[r]["rest_time"],i)
        max_distance = max(values.values())
        for r in values:
            if values[r] == max_distance:
                scores[r] += 1

    print(max(scores.values()))


                






