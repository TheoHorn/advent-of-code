import re
from itertools import permutations

def scores(array, repartition):
    values = [0] * len(array[0])
    for i, quantity in enumerate(repartition):
        for j in range(len(values)):
            values[j] += quantity * array[i][j]
    if any(value < 0 for value in values):
        return 0
    result = 1
    for value in values:
        result *= value
    return result


with open("2015/15/input.txt") as f:
    lines = f.readlines()
    array = []
    for line in lines:
        matches = re.findall(r'-?\d+', line)
        matches = [int(x) for x in matches]
        array.append(matches[:-1])  # Ignore calories

    nb_teespoon = 100
    num_ingredients = len(array)
    best_score = 0

    for repartition in permutations(range(nb_teespoon + 1), num_ingredients):
        if sum(repartition) == nb_teespoon:
            score = scores(array, repartition)
            if score > best_score:
                best_score = score
                print(f"New best repartition: {repartition}, score: {best_score}")

    print("Best score:", best_score)


