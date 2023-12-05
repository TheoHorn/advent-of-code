
with open('2023/day5/input.txt') as f:
    lines = f.read().splitlines()
    count = 0
    list_seed = []
    list_seed_to_soil = []
    list_soil_to_fertilizer = []
    list_fertilizer_to_water = []
    list_water_to_light = []
    list_light_to_temperature = []
    list_temperature_to_humidity = []
    list_humidity_to_location = []


    seed = lines[0].split(' ')
    for i in range(1,len(seed)):
        list_seed.append(int(seed[i]))
    j = 2
    while lines[j] != '!':
        list_seed_to_soil.append(lines[j])
        j += 1
    j += 1
    while lines[j] != '!':
        list_soil_to_fertilizer.append(lines[j])
        j += 1
    j += 1
    while lines[j] != '!':
        list_fertilizer_to_water.append(lines[j])
        j += 1
    j += 1
    while lines[j] != '!':
        list_water_to_light.append(lines[j])
        j += 1
    j += 1
    while lines[j] != '!':
        list_light_to_temperature.append(lines[j])
        j += 1
    j += 1
    while lines[j] != '!':
        list_temperature_to_humidity.append(lines[j])
        j += 1
    j += 1
    while j < len(lines):
        list_humidity_to_location.append(lines[j])
        j += 1
    

    nl = []
    for seed in list_seed:
        for seed_to_soil in list_seed_to_soil[1:]:
            soil = seed_to_soil.split(' ')
            if seed >= int(soil[1]) and seed <= int(soil[1])+int(soil[2]):
                seed = int(soil[0]) + (seed - int(soil[1]))
                break
        print(seed)
        for soil_to_fertilizer in list_soil_to_fertilizer[1:]:
            fertilizer = soil_to_fertilizer.split(' ')
            if seed >= int(fertilizer[1]) and seed <= int(fertilizer[1])+int(fertilizer[2]):
                seed = int(fertilizer[0]) + (seed - int(fertilizer[1]))
                break
        print(seed)
        for fertilizer_to_water in list_fertilizer_to_water[1:]:
            water = fertilizer_to_water.split(' ')
            if seed >= int(water[1]) and seed <= int(water[1])+int(water[2]):
                seed = int(water[0]) + (seed - int(water[1]))
                break
        print(seed)
        for water_to_light in list_water_to_light[1:]:
            light = water_to_light.split(' ')
            if seed >= int(light[1]) and seed <= int(light[1])+int(light[2]):
                seed = int(light[0]) + (seed - int(light[1]))
                break
        print(seed)
        for light_to_temperature in list_light_to_temperature[1:]:
            temperature = light_to_temperature.split(' ')
            if seed >= int(temperature[1]) and seed <= int(temperature[1])+int(temperature[2]):
                seed = int(temperature[0]) + (seed - int(temperature[1]))
                break
        print(seed)
        for temperature_to_humidity in list_temperature_to_humidity[1:]:
            humidity = temperature_to_humidity.split(' ')
            if seed >= int(humidity[1]) and seed <= int(humidity[1])+int(humidity[2]):
                seed = int(humidity[0]) + (seed - int(humidity[1]))
                break
        print(seed)
        for humidity_to_location in list_humidity_to_location[1:]:
            location = humidity_to_location.split(' ')
            if seed >= int(location[1]) and seed <= int(location[1])+int(location[2]):
                seed = int(location[0]) + (seed - int(location[1]))
                break
        nl.append(seed)
    print(nl)
    ans = min(nl)
    print(ans)


        