import math


f = open('2023/day4/input.txt', 'r')
txt = f.read().split('\n')
sum = 0
dico = {}
for i in range(len(txt)):
    ligne = txt[i].split(':')
    dico[i] = 1

for i in range(len(txt)):
    print(dico[i])
    for k in range(dico[i]):
        num = 1
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
        
        #add to dico
        for l in range(len(liste)):
            if i+num >= 198:
                print("error")
                break
            if liste[l] in listefinal:
                #print(i,":",liste[l],listefinal,"->",i+num)
                dico[i+num] = dico[i+num] + 1
                num = num + 1
sum = 0
for i in dico:
    sum = sum + dico[i]
print(sum)