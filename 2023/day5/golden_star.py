import copy

def split_bounds(dico, bounds_origin):
    ans = []
    bounds = copy.deepcopy(bounds_origin)

    while bounds:
        current_bounds = bounds.pop()
        min, max = current_bounds
        changed = False
        for min_dico, max_dico in dico.keys():
            bounds_dico = dico[(min_dico, max_dico)]
            if min_dico <= min <= max_dico and min_dico <= max <= max_dico:
                ans.append((bounds_dico + min - min_dico, bounds_dico + max - min_dico))
                changed = True
            elif min_dico <= max <= max_dico:
                ans.append((bounds_dico, bounds_dico + max - min_dico))
                bounds.append((min, min_dico - 1))
                changed = True
            elif min_dico <= min <= max_dico:
                ans.append((bounds_dico + min - min_dico, bounds_dico + max_dico - min_dico))
                bounds.append((max_dico + 1, max))
                changed = True
            elif min < min_dico and max > max_dico:
                ans.append((bounds_dico, bounds_dico + max_dico - min_dico))
                bounds.append((min, min_dico - 1))
                bounds.append((max_dico + 1, max))
                changed = True
        if not changed:
            ans.append((min, max))

    return ans
    

def principal():
    f = open('2023/day5/input.txt')
    lines = f.read().splitlines()

    seed_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temperature = {}
    temperature_to_humidity = {}
    humidity_to_location = {}

    seed = lines[0].split(' ')
    seeds = []
    for i in range(1, len(seed), 2):
        seeds.append((int(seed[i]),int(seed[i]) + int(seed[i + 1])))

    j = 3
    while lines[j] != '!':
        line = lines[j].split(' ')
        seed_to_soil.update({(int(line[1]), int(line[1]) + int(line[2])): int(line[0])})
        j += 1

    j += 2
    while lines[j] != '!':
        line = lines[j].split(' ')
        soil_to_fertilizer.update({(int(line[1]), int(line[1]) + int(line[2])): int(line[0])})
        j += 1

    j += 2
    while lines[j] != '!':
        line = lines[j].split(' ')
        fertilizer_to_water.update({(int(line[1]), int(line[1]) + int(line[2])): int(line[0])})
        j += 1

    j += 2
    while lines[j] != '!':
        line = lines[j].split(' ')
        water_to_light.update({(int(line[1]), int(line[1]) + int(line[2])): int(line[0])})
        j += 1

    j += 2
    while lines[j] != '!':
        line = lines[j].split(' ')
        light_to_temperature.update({(int(line[1]), int(line[1]) + int(line[2])): int(line[0])})
        j += 1

    j += 2
    while lines[j] != '!':
        line = lines[j].split(' ')
        temperature_to_humidity.update({(int(line[1]), int(line[1]) + int(line[2])): int(line[0])})
        j += 1

    j += 2
    while j  < len(lines):
        line = lines[j].split(' ')
        humidity_to_location.update({(int(line[1]), int(line[1]) + int(line[2])): int(line[0])})
        j += 1

    seeds = split_bounds(seed_to_soil, seeds)
    seeds = split_bounds(soil_to_fertilizer, seeds)
    seeds = split_bounds(fertilizer_to_water, seeds)
    seeds = split_bounds(water_to_light, seeds)
    seeds = split_bounds(light_to_temperature, seeds)
    seeds = split_bounds(temperature_to_humidity, seeds)
    seeds = split_bounds(humidity_to_location, seeds)

    return min(seeds)[0]

print(principal())
