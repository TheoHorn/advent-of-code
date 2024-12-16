import re
from itertools import combinations

with open("2015/24/input.txt") as f:
    ctn = f.read()
    numbers = re.findall(r'\d+', ctn)

numbers = list(map(int, numbers))

target_weight = sum(numbers) // 4

def find_groups(numbers, target_weight):
    for i in range(len(numbers)):
        for group in combinations(numbers, i):
            if sum(group) == target_weight:
                remaining_numbers = list(numbers)
                for num in group:
                    remaining_numbers.remove(num)
                yield group, remaining_numbers

def can_partition(remaining_numbers, target_weight):
    for group, _ in find_groups(remaining_numbers, target_weight):
        return True
    return False

minimum_size = len(numbers)
best_group = None
lowest_multiplication = float('inf')

for group1, remaining_numbers1 in find_groups(numbers, target_weight):
    if len(group1) < minimum_size and can_partition(remaining_numbers1, target_weight):
        minimum_size = len(group1)
        multiplication = 1
        for num in group1:
            multiplication *= num
        if multiplication < lowest_multiplication:
            lowest_multiplication = multiplication
            best_group = group1

print("Lowest QE:", lowest_multiplication)
print("Best group:", best_group)
