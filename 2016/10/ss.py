import re

with open("2016/10/input.txt") as f:
    lines = f.read().splitlines()

low_chip = 17
high_chip = 61
processes = {}
bots = {}
two_value_bots = []

for line in lines:
    if line.startswith("bot"):
        values = list(map(int, re.findall(r'\d+', line)))
        processes[values[0]] = (values[1],values[2])
    else:
        values = list(map(int, re.findall(r'\d+', line)))
        if values[1] in bots:
            bots[values[1]].append(values[0])
        else:
            bots[values[1]] = [values[0]]
        
        if len(bots[values[1]]) == 2:
            two_value_bots.append(values[1])

found = False
while not found:
    # Get a bot with twos values
    two_value = two_value_bots.pop(0)

    # Get the two values
    values = bots[two_value]
    low = min(values)
    high = max(values)
    bots[two_value] = []

    if low == low_chip and high == high_chip:
        print(f"The bot comapring {low_chip} and {high_chip} is {two_value}")
        break
    # Get the two bot
    (bot_low,bot_high) = processes[two_value]

    # Add the data
    if bot_low in bots:
        bots[bot_low].append(low)
    else:
        bots[bot_low] = [low]

    if bot_high in bots:
        bots[bot_high].append(high)
    else:
        bots[bot_high] = [high]

    # Add if there are at two in it now
    if len(bots[bot_low]) == 2:
        two_value_bots.append(bot_low)
    if len(bots[bot_high]) == 2:
        two_value_bots.append(bot_high)

