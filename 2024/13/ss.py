import re
from math import gcd
from itertools import combinations

with open("2024/13/input.txt") as f:
    lines = f.readlines()
    machines = []
    for i in range(0, len(lines), 4):
        machine = []
        a = lines[i]
        b = lines[i+1]
        prize = lines[i+2]
        a_numbers = re.findall(r'\d+',a)
        b_numbers = re.findall(r'\d+', b)
        prize_numbers = re.findall(r'\d+', prize)
        machine.append((int(a_numbers[0]), int(a_numbers[1])))
        machine.append((int(b_numbers[0]), int(b_numbers[1])))
        machine.append((int(prize_numbers[0]), int(prize_numbers[1])))
        machines.append(machine)


cost = [3,1]
results = 0

for machine in machines:
    # Extract machine parameters
    (x_a, y_a) = machine[0]
    (x_b, y_b) = machine[1]
    (x_prize, y_prize) = machine[2]
    biggest_x = max(x_prize // x_a, x_prize // x_b)
    biggest_y = max(y_prize // y_a, y_prize // y_b)

    current_cost = float('inf')
    found = False
    for i in range(biggest_x + 1):
        for j in range(biggest_y + 1):
            x_found = i * x_a + j * x_b
            y_found = i * y_a + j * y_b
            if x_found == x_prize and y_found == y_prize:
                cost_found = i * cost[0] + j * cost[1]
                if cost_found < current_cost:
                    current_cost = cost_found
                found = True
    if found:
        results += current_cost
print(results)
