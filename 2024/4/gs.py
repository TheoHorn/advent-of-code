with open("2024/4/input.txt") as f:
    data = [list(line.strip()) for line in f]
    nb = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if j > 0 and i > 0 and j < len(data[0])-1 and i < len(data)-1:
                if data[i][j]=='A' and data[i-1][j+1]=='M' and  data[i-1][j-1]=='M' and data[i+1][j-1]=='S' and data[i+1][j+1]=='S' :   # MM haut
                    nb +=1
                if data[i][j]=='A' and data[i-1][j+1]=='M' and  data[i-1][j-1]=='S' and data[i+1][j-1]=='S' and data[i+1][j+1]=='M' :   # SM haut
                    nb +=1
                if data[i][j]=='A' and data[i-1][j+1]=='S' and  data[i-1][j-1]=='S' and data[i+1][j-1]=='M' and data[i+1][j+1]=='M' :   # SS haut
                    nb +=1
                if data[i][j]=='A' and data[i-1][j+1]=='S' and  data[i-1][j-1]=='M' and data[i+1][j-1]=='M' and data[i+1][j+1]=='S' :   # MS haut
                    nb +=1
                
                
    print(nb)
