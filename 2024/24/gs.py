import re
from random import randint
from collections import defaultdict

# Load the input data
with open("2024/24/input.txt", "r") as file:
    raw_wire_values_data, raw_connections_data = file.read().split("\n\n")
    initial_wire_values = raw_wire_values_data.split("\n")
    connections = raw_connections_data.split("\n")

# Data structures initialization
wire_values = {}           # Maps wire names to their current values or operations
evaluated_results = {}     # Stores the evaluated results for wires
initial_wires = set()      # Set of wires with fixed values
x_wires = set()            # Set of wires corresponding to 'x' values
y_wires = set()            # Set of wires corresponding to 'y' values
output_wires = set()       # Set of output wires to track
all_wires = set()          # Set of all wires used in the system
visited_wires = defaultdict(bool)  # Keeps track of which wires have been visited during evaluation

# Parse initial wire values and categorize them
for line in initial_wire_values:
    wire_name = line[:3]
    wire_value = int(line[5:])
    wire_values[wire_name] = wire_value
    evaluated_results[wire_name] = wire_value
    all_wires.add(wire_name)
    initial_wires.add(wire_name)
    if wire_name[0] == 'x':
        x_wires.add(wire_name)
    else:
        y_wires.add(wire_name)

# Parse wire connections (operations between wires)
for line in connections:
    if line.strip() == "":  # Skip empty lines
        continue
    parts = line.split(" ")
    input_wire1 = parts[0]
    operation = parts[1]
    input_wire2 = parts[2]
    output_wire = parts[4]

    if re.match(r'z[0-9][0-9]', output_wire):  # Identifying output wires
        output_wires.add(output_wire)
    
    wire_values[output_wire] = (input_wire1, operation, input_wire2)
    all_wires.update({input_wire1, input_wire2, output_wire})

# Optimized function to convert a number to binary digits (least significant bit first)
def to_binary(number):
    # Convert the number to binary, remove the '0b' prefix, and reverse the string
    return [int(bit) for bit in bin(number)[2:][::-1]]

# Evaluate the value of a wire using recursion
def evaluate_wire(wire, wire_mapping):
    if wire not in initial_wires:
        mapped_wire = wire_mapping.get(wire, wire)

        if wire in evaluated_results and evaluated_results[wire] != -1:
            return evaluated_results[wire]

        input_wire1, operation, input_wire2 = wire_values[mapped_wire]
        
        if visited_wires[wire]:  # To prevent circular dependencies
            return -1
        
        visited_wires[wire] = True

        # Evaluate the input wires recursively
        if evaluate_wire(input_wire1, wire_mapping) == -1 or evaluate_wire(input_wire2, wire_mapping) == -1:
            return -1

        # Perform the operation based on the gate type
        if operation == "AND":
            result = evaluated_results[input_wire1] & evaluated_results[input_wire2]
        elif operation == "OR":
            result = evaluated_results[input_wire1] | evaluated_results[input_wire2]
        elif operation == "XOR":
            result = evaluated_results[input_wire1] ^ evaluated_results[input_wire2]
        else:
            result = -1

        evaluated_results[wire] = result
        return result
    else:
        return evaluated_results[wire]

# Set input values for x and y wires based on binary representation
def set_inputs(x, y):
    x_binary = to_binary(x)
    y_binary = to_binary(y)

    # Assign values to x and y wires
    for i, wire in enumerate(sorted(x_wires)):
        evaluated_results[wire] = x_binary[i] if i < len(x_binary) else 0
    for i, wire in enumerate(sorted(y_wires)):
        evaluated_results[wire] = y_binary[i] if i < len(y_binary) else 0

    # Set initial values for other wires that are not part of the initial values
    for wire in all_wires:
        if wire not in initial_wires:
            evaluated_results[wire] = -1

    # Reset visited wires state
    for key in visited_wires.keys():
        visited_wires[key] = False

# Evaluate the system's performance with random inputs
def evaluate_system_performance(wire_mapping):
    random_x_inputs = [randint(0, max_x_value) for _ in range(100)]
    random_y_inputs = [randint(0, max_y_value) for _ in range(100)]
    total_score = 0

    for i in range(100):
        set_inputs(random_x_inputs[i], random_y_inputs[i])
        output_values = [evaluate_wire(output, wire_mapping) for output in sorted(output_wires)]

        if -1 in output_values:  # If evaluation fails for any output wire, return an infinite score
            return float("inf")

        expected_result = to_binary(random_x_inputs[i] + random_y_inputs[i])
        expected_result += [0] * (len(output_values) - len(expected_result))  # Ensure same length

        # Count the number of differing bits between the output and expected result
        total_score += sum(1 for j in range(len(output_values)) if output_values[j] != expected_result[j])

    return total_score

# Swap two wires in the mapping
def swap_wires(mapping, wire1, wire2):
    temp1 = mapping.get(wire1, wire1)
    temp2 = mapping.get(wire2, wire2)
    mapping[wire1] = temp2
    mapping[wire2] = temp1

# Main logic
output_wires = sorted(output_wires)
max_x_value = 2 ** len(x_wires)
max_y_value = 2 ** len(y_wires)

# Track wires swapped in each iteration
swapped_wires_history = []

# Perform 4 iterations of wire swapping
for iteration in range(4):
    best_score = evaluate_system_performance({})
    best_mapping = {}
    good_connections = defaultdict(list)

    # Identify potentially good wire connections
    for wire1 in all_wires:
        if wire1 in initial_wires:
            continue
        for wire2 in all_wires:
            if wire1 >= wire2 or wire2 in initial_wires or wire2 in good_connections[wire1]:
                continue

            set_inputs(0, 0)
            temp_mapping = {}
            swap_wires(temp_mapping, wire1, wire2)

            if -1 not in [evaluate_wire(output, temp_mapping) for output in sorted(output_wires)]:
                good_connections[wire1].append(wire2)

    # Optimize wire mappings
    total_wires = len(all_wires)
    current_wire_index = 0

    for wire1 in all_wires:
        if wire1 in initial_wires:
            current_wire_index += 1
            continue

        print(f"Iteration {iteration + 1}/4 - Progress: {current_wire_index / total_wires * 100:.2f}%")
        current_wire_index += 1

        for wire2 in good_connections[wire1]:
            temp_mapping = {}
            swap_wires(temp_mapping, wire1, wire2)
            score = evaluate_system_performance(temp_mapping)

            if score < best_score:
                best_score = score
                best_mapping = temp_mapping.copy()
                print(f"Updating best mapping: {best_mapping}")

    # Store the swapped wires for this iteration
    swapped_wires = [(wire1, wire2) for wire1, wire2 in best_mapping.items()]
    swapped_wires_history.append(swapped_wires)

    # Apply the best mapping definitively
    for wire1, wire2 in best_mapping.items():
        wire_values[wire1] = wire_values.get(wire2, wire2)

# Final output
print("All swapped wires:")
all_swapped_wires = set()
for swapped_wires in swapped_wires_history:
    all_swapped_wires.update(swapped_wires)

sorted_all_swapped_wires = sorted(all_swapped_wires, key=lambda x: (x[0], x[1]))
print(sorted_all_swapped_wires)
