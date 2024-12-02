with open("2024/day2/input.txt") as f:
    lines = f.readlines()
    safe = 0
    for line in lines:
        tab = line.split(" ")
        
        tab = list(map(int, tab))
        print(tab)
        if tab[0] < tab[1]: increase = True
        elif tab[0] > tab[1]: increase = False
        else: continue

        notsafe = False
        for i in range(1,len(tab)): 
            diff = tab[i] - tab[i-1]
            print(f"diff: {tab[i]} - {tab[i-1]} = {diff}")
            if(increase):
                if(not(diff > 0 and diff < 4)):
                    notsafe = True
                    break
            else:
                if(not(diff < 0 and diff > -4)): 
                    notsafe= True
                    break
        if not(notsafe): safe += 1
    print(safe)