from itertools import combinations
from itertools import product

with open("2024/7/input.txt") as f:
    ctn = f.readlines()
    dico = {}
    for line in ctn: 
        words = line.split(" ")
        dico[int(words[0][:-1])] = list(map(int, words[1:]))

ops = ['+', '*','||']

def apply_operations(numbers, operations):
    result = numbers[0]
    for num, op in zip(numbers[1:], operations):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '||':
            result = int(str(result)+str(num))
    return result
summed = 0
for key, value in dico.items():
    for combination in combinations(value, len(value)):
        for operations in product(ops, repeat=len(value)-1):
            result = apply_operations(combination, operations)
            if result == key:
                summed += key
                break

print(summed)