ans = 0

with open('2015/day5/input.txt', 'r') as f:
    txt = f.read().split('\n')
    for i in range(len(txt)):
        mot = txt[i]
        for k in range(len(mot)-2):
            nmot = mot[k:k+2]
            if nmot in mot[k+2:]:
                for j in range(len(mot)):
                    if j+2 < len(mot) and mot[j] == mot[j+2]:
                        ans = ans + 1
                        print(nmot, "->", mot[k+2:])
                        break
                break
#           else:
#               print(nmot, "-/>", mot[k+2:])
print(ans)