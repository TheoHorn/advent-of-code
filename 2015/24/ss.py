import re
from itertools import combinations

with open("2015/24/input.txt") as f:
    ctn = f.read()
    numbers = re.findall(r'\d+', ctn)

numbers = list(map(int, numbers))

target_weight = sum(numbers)//3

minimum_size = len(numbers)
def find_groups(numbers, target_weight):
    for i in range(len(numbers)):
        for group in combinations(numbers, i):
            if sum(group) == target_weight:
                remaining_numbers = list(numbers)
                for num in group:
                    remaining_numbers.remove(num)
                yield group, remaining_numbers

all_possibilities = []
for group1, remaining_numbers1 in find_groups(numbers, target_weight):
    if len(group1) < minimum_size:
        minimum_size = len(group1)
        all_possibilities.clear()
        for group2, remaining_numbers2 in find_groups(remaining_numbers1, target_weight):
            group3 = remaining_numbers2
            all_possibilities.append((group1,group2,group3))


# Example of how to use all_possibilities
lowest_multiplication = float('inf')
best_group = None

for group1, group2, group3 in all_possibilities:
    multiplication = 1
    for num in group1:
        multiplication *= num
    if multiplication < lowest_multiplication:
        lowest_multiplication = multiplication
        best_group = (group1, group2, group3)

print("Lowest QE:", lowest_multiplication)
print("Best group:", best_group)