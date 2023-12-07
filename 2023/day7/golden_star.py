def compare(main1,main2):
    letters = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    letters.reverse()
    count_main1 = []
    count_main2 = []
    countj1 = 0
    countj2 = 0
    for letter in letters:
        if letter != 'J':
            count_main1.append(main1.count(letter))
            count_main2.append(main2.count(letter))
        else:
            countj1 = main1.count(letter)
            countj2 = main2.count(letter)   
    count_main1.sort()
    count_main2.sort()
    count_main1.reverse()
    count_main2.reverse()
    count_main1[0] += countj1
    count_main2[0] += countj2
    if count_main1 > count_main2:
        return True
    elif count_main1 < count_main2:
        return False
    else:
        string = main1
        string2 = main2
        for j in range(len(string)):
            if string[j] == 'T':
                v1 = 10
            elif string[j] == 'J':
                v1 = 1
            elif string[j] == 'Q':
                v1 = 12
            elif string[j] == 'K':
                v1 = 13
            elif string[j] == 'A':
                v1 = 14
            else :
                v1 = int(string[j])

            if string2[j] == 'T':
                v2 = 10
            elif string2[j] == 'J':
                v2 = 1
            elif string2[j] == 'Q':
                v2 = 12
            elif string2[j] == 'K':
                v2 = 13
            elif string2[j] == 'A':
                v2 = 14
            else :
                v2 = int(string2[j])

            if v1 > v2:
                return True
            elif v1 < v2:
                return False

compare('KK222','KKTTT')
with open('2023/day7/input.txt') as f:
    lines = f.read().splitlines()
    dico={}
    for line in lines:
        line = line.split(' ')
        dico.update({line[0]:line[1]})
    
    l = []
    for key in dico:
        i = 0
        while i < len(l):
            main = l[i]
            if compare(key, main):
                l.insert(i, key)
                break
            i += 1
        if i == len(l):
            l.append(key)
    
    somme = 0
    for v in l:
        i = len(l)- l.index(v)
        somme += i * int(dico[v])
        print(v, int(dico[v]), somme)
    print(somme)