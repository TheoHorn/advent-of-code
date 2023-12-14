input = "cqjxjnds"

def verif_password(input):
    if "i" in input or "o" in input or "l" in input:
        return False
    
    for i in range(len(input)-2):
        if ord(input[i]) == ord(input[i+1]) - 1 and ord(input[i]) == ord(input[i+2]) - 2:
            break
        else:
            return False

    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            for j in range(i+2, len(input)-1):
                if input[j] == input[j+1]:
                    return True
    return False

def next_password(inp):
    i = len(inp) - 1
    bool = True
    while verif_password(inp) or bool:
        bool = False
        if inp[i] == 'z':
            inp = inp[:i] + 'a' + inp[i+1:]
            i = i-1
        else:
            inp = inp[:i] + chr(ord(inp[i])+1) + inp[i+1:]
    print(inp)

print(ord('a'))
next_password(input)    
    

        
