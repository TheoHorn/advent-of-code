ans = 0

with open('2015/day5/input.txt', 'r') as f:
    txt = f.read().split('\n')
    for i in range(len(txt)):
        mot = txt[i]
        if mot.count('a') + mot.count('e') + mot.count('i') + mot.count('o') + mot.count('u') < 3:
            continue
        if mot.rfind('ab') != -1 or mot.rfind('cd') != -1 or mot.rfind('pq') != -1 or mot.rfind('xy') != -1:
            continue
        for j in range(len(mot)-1):
            if mot[j] == mot[j+1]:
                ans = ans + 1
                break
print(ans)