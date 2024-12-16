with open("2015/23/input.txt")as f:
    lines = f.readlines()

a = 0
b = 0

i = 0
while i < len(lines):
    line = lines[i]
    values = line.split()
    if len(values) == 2:
        op = values[0]
        val = values[1]
        if op == "inc":
            if val == "a":
                a += 1
            elif val == "b":
                b += 1
        elif op == "hlf":
            if val == "a":
                a //= 2
            elif val == "b":
                b //= 2
        elif op == "tpl":
            if val == "a":
                a *= 3
            elif val == "b":
                b *= 3
        else:
            i += int(val)-1
    else:
        op = values[0]
        reg = values[1]
        val = values[2]
        if op == "jie":
            if reg == "a,":
                if a % 2 == 0:
                    i += int(val)-1
            elif reg == "b,":
                if b % 2 == 0:
                    i += int(val)-1
        elif op == "jio":
            if reg == "a,":
                if a == 1:
                    i += int(val)-1
            elif reg == "b,":
                if b == 1:
                    i += int(val)-1
    i += 1
print(b)
