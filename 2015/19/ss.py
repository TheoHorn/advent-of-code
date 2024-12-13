from collections import defaultdict
import re

with open("2015/19/input.txt") as f:
    lines = f.readlines()
    molecule = lines[-1].strip()
    rules = defaultdict(list)
    for line in lines[:-2]:
        elem = line.strip().split(" => ")
        rules[elem[0]].append(elem[1])

unique_molecule = set()
for key, values in rules.items():
    for rule in values:
        for match in re.finditer(key, molecule):
            new_molecule = molecule[:match.start()] + rule + molecule[match.end():]
            unique_molecule.add(new_molecule)

print(len(unique_molecule))