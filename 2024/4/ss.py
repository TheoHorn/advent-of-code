with open("2024/4/input.txt") as f:
    data = [list(line.strip()) for line in f]
    nb = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if j+3<len(data[0]) and data[i][j]=='X' and data[i][j+1]=='M' and  data[i][j+2]=='A' and  data[i][j+3]=='S':   # Droite
                nb+=1
            if j-3>=0 and data[i][j]=='X' and data[i][j-1]=='M' and  data[i][j-2]=='A' and  data[i][j-3]=='S':   # Gauche
                nb+=1
            if i+3<len(data) and data[i][j]=='X' and data[i+1][j]=='M' and  data[i+2][j]=='A' and  data[i+3][j]=='S':   # Haut
                nb+=1
            if i-3>=0 and data[i][j]=='X' and data[i-1][j]=='M' and  data[i-2][j]=='A' and  data[i-3][j]=='S':   # Bas
                nb+=1
            if i+3<len(data) and j+3<len(data[0]) and data[i][j]=='X' and data[i+1][j+1]=='M' and  data[i+2][j+2]=='A' and  data[i+3][j+3]=='S':   # Bas droit
                nb+=1
            if i+3<len(data) and j-3>=0 and data[i][j]=='X' and data[i+1][j-1]=='M' and  data[i+2][j-2]=='A' and  data[i+3][j-3]=='S':   # Bas Gauche
                nb+=1
            if i-3>=0 and j-3>=0 and data[i][j]=='X' and data[i-1][j-1]=='M' and  data[i-2][j-2]=='A' and  data[i-3][j-3]=='S':   #Haut Gauche
                nb+=1
            if i-3>=0 and j+3<len(data[0]) and data[i][j]=='X' and data[i-1][j+1]=='M' and  data[i-2][j+2]=='A' and  data[i-3][j+3]=='S':   #Haut droite
                nb+=1
    print(nb)
