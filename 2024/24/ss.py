dico = {}

# Read the input file and split it into two parts
with open("2024/24/input.txt") as f:
    ctn = f.read().split("\n\n")

# Parse the first part to populate the dictionary with initial values
for line in ctn[0].split("\n"):
    key, value = line.split(": ")
    dico[key] = int(value)
print(dico)

# Parse the second part to get the list of gate operations
instructions = [line.split(" -> ") for line in ctn[1].split("\n")]
# Process the instructions until all are resolved
while instructions:
    remaining_instructions = []
    for calcul, res in instructions:
        try:
            if "XOR" in calcul:
                a, b = calcul.split(" XOR ")
                dico[res] = dico[a] ^ dico[b]
            elif "OR" in calcul:
                a, b = calcul.split(" OR ")
                dico[res] = dico[a] | dico[b]
            elif "AND" in calcul:
                a, b = calcul.split(" AND ")
                dico[res] = dico[a] & dico[b]
        except KeyError:
            # Defer the instruction if required inputs are not yet resolved
            remaining_instructions.append((calcul, res))
    
    instructions = remaining_instructions

z_items = {key: dico[key] for key in dico if key.startswith('z')}
sorted_z_items = dict(sorted(z_items.items(),reverse=True))

binary = "".join(str(sorted_z_items[key]) for key in sorted_z_items)
decimal_value = int(binary, 2)

print(decimal_value)
