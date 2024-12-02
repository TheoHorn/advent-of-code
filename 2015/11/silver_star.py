import re
valt = "cqjxjnds"

def verif_password(input):
    if "i" in input or "o" in input or "l" in input:
        return False

    if len(re.findall(r'(\w)\1', input)) < 2:
        return False

    for i in range(len(input) - 2):
        if ord(input[i]) + 1 == ord(input[i + 1]) and ord(input[i + 1]) + 1 == ord(input[i + 2]):
            return True
    return False

def next_password(inp):
    inp = list(inp)
    while not verif_password("".join(inp)):
        i = len(inp) - 1
        while i >= 0:
            if inp[i] == 'z':
                inp[i] = 'a'
                i -= 1
            else:
                inp[i] = chr(ord(inp[i]) + 1)
                break
    return "".join(inp)


print(next_password("cqjxxzaa"))
    

        
