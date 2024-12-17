import re

# Read input from file
with open("2024/17/input.txt") as f:
    ctn = f.read()
    numbers = re.findall(r"\d+", ctn)
    A = int(numbers[0])
    B = int(numbers[1])
    C = int(numbers[2])
    PROGRAM = numbers[3:]
    inputing = ",".join(PROGRAM) + ","

# PART 2
numbers = PROGRAM[:]
numbers = list(map(int, numbers))

def solve(size, res, a, b, c):
    print(size, res)
    if size < 0:
        return True
    for bits in range(8):
        a = res * 8 | bits
        i = 0
        while i < len(numbers):
            op = numbers[i]
            combo = numbers[i+1]

            # Combo to val
            if combo <= 3:
                val = combo
            elif combo == 4:
                val = a
            elif combo == 5:
                val = b
            elif combo == 6:
                val = c

            # Operations
            if op == 0:
                a = a // 2**val
            elif op == 1:
                b ^= combo
            elif op == 2:
                b = val % 8
            elif op == 3:
                i = combo - 2 if a != 0 else i
            elif op == 4:
                b ^= c
            elif op == 5:
                w = val % 8
                break
            elif op == 6:
                b = a // 2**val
            elif op == 7:
                c = a // 2**val
            i += 2
        if w == numbers[size] and solve(size - 1, res << 3 | bits, a, b, c):
            return True
    return False

solve(len(numbers) - 1, 0, 0, 0, 0)


