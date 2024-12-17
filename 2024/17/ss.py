import re 
with open("2024/17/input.txt") as f:
    ctn = f.read()
    numbers = re.findall(r"\d+", ctn)
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])
    program = numbers[3:]

def litteral_to_combo(x):
    if x == 4:
        result = a
    elif x == 5:
        result = b
    elif x == 6:
        result = c
    else:
        result = x
    return result


i = 0
output = "out : "
while i< len(program):

    op = int(program[i])
    val = int(program[i+1])
    if op == 0:
        # Perform division
        a = a // 2**litteral_to_combo(val)
    elif op == 1:
        # Perform bitwise b XOR val
        b = b ^ val
    elif op == 2:
        # Perform modulo 8
        b = litteral_to_combo(val) % 8
    elif op == 3:
        # jumps if A not 0
        if a != 0:
            i = val- 2 
    elif op == 4:
        # Perform bitwise b XOR c
        b = b ^ c
    elif op == 5:
        # Perform print
        output += str(litteral_to_combo(val) % 8)+","
    elif op == 6:
        # Perform division into B
        b = a // 2**litteral_to_combo(val)
    elif op == 7:
        # Perform bitwise into c
        c = a // 2**litteral_to_combo(val)

    print(f"Step {i}: a={a}, b={b}, c={c}, op={op}, val={val}")
    i += 2
print(output)