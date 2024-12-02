import math


f = open('day4/input.txt', 'r')
txt = f.read().split('\n')
sum = 0
for i in range(len(txt)):
    ligne = txt[i].split(' ')
    liste = []
    listefinal = []
    bool = False
    for j in range(2,len(ligne)):
        if ligne[j] == '|':
            bool = True
            continue
        else:
            if bool:
                listefinal.append(ligne[j])
            else:
                liste.append(ligne[j])
    for i in range(3):
        if '' in liste:
            liste.remove('')
        if '' in listefinal:
            listefinal.remove('')
    power = -1
    val = 0
    for k in range(len(liste)):
        if liste[k] in listefinal:
            power = power +1
            val = 2**power
    print(val)
    sum += val
print(sum)