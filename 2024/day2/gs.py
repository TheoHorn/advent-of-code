def check_sequence(tab):
    increasing = tab[1] > tab[0]
    for i in range(len(tab) - 1):
        diff = tab[i + 1] - tab[i]
        if increasing:
            if not (1 <= diff <= 3):
                return False
        else:
            if not (-3 <= diff <= -1):
                return False
    return True


with open("2024/day2/input.txt") as f:
    lines = f.readlines()
    safe = 0
    for line in lines:
        tab = list(map(int, line.split()))
        notsafe = True
        if check_sequence(tab):
            notsafe = False
        
        for i in range(len(tab)):
            if check_sequence(tab[:i] + tab[i + 1:]):
                notsafe = False

        if not(notsafe):safe += 1
    print(safe)
