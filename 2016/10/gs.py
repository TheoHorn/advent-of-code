import re

with open("2016/10/input.txt") as f:
    lines = f.read().splitlines()

processes = {}
bots = {}
two_value_bots = []

outputs = {}

for line in lines:
    if line.startswith("bot"):
        values = list(map(int, re.findall(r'\d+', line)))
        processes[values[0]] = (values[1], values[2], line.split()[5], line.split()[-2])
    else:
        values = list(map(int, re.findall(r'\d+', line)))
        if values[1] in bots:
            bots[values[1]].append(values[0])
        else:
            bots[values[1]] = [values[0]]
        
        if len(bots[values[1]]) == 2:
            two_value_bots.append(values[1])

found = False
while len(two_value_bots) != 0:
    # Get a bot with two values
    two_value = two_value_bots.pop(0)

    # Get the two values
    values = bots[two_value]
    low = min(values)
    high = max(values)
    bots[two_value] = []
    
    # Get the two bot or output
    (bot_low, bot_high, low_type, high_type) = processes[two_value]

    # Add the data
    if low_type == "bot":
        if bot_low in bots:
            bots[bot_low].append(low)
        else:
            bots[bot_low] = [low]
        if len(bots[bot_low]) == 2:
            two_value_bots.append(bot_low)
    else:
        if bot_low in outputs:
            outputs[bot_low].append(low)
        else:
            outputs[bot_low] = [low]

    if high_type == "bot":
        if bot_high in bots:
            bots[bot_high].append(high)
        else:
            bots[bot_high] = [high]
        if len(bots[bot_high]) == 2:
            two_value_bots.append(bot_high)
    else:
        if bot_high in outputs:
            outputs[bot_high].append(high)
        else:
            outputs[bot_high] = [high]

result = outputs[0][0] * outputs[1][0] * outputs[2][0]
print(result)