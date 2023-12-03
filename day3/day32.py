f = open('day3/input.txt', 'r')
txt = f.read().split('\n')
sum = 0
mult = {}
for i in range(len(txt)):
    
    j = 0
    while j < len(txt[i]):
        num = ''
        while j < len(txt[i]) and txt[i][j].isdigit():
            num += txt[i][j]
            j += 1

        if num:
            bool = False
            for k in range(len(num)):
                j = j-1
                #top
                if 0 <= i-1 < len(txt) and 0 <= j-k < len(txt[i-1]) and txt[i-1][j-k] == '*':
                    if (i-1, j-k) in mult:
                        mult[(i-1,j-k)] =  (int(num)* mult[(i-1, j-k)][0],2)
                    else:
                        mult[(i-1, j-k)] = (int(num), 1)
                    break
                    

                #bottom
                if 0 <= i+1 < len(txt) and 0 <= j-k < len(txt[i+1]) and txt[i+1][j-k] == '*':
                    if (i+1, j-k) in mult:
                        mult[(i+1,j-k)] =  (int(num)* mult[(i+1, j-k)][0],2)
                    else:
                        mult[(i+1, j-k)] = (int(num), 1)
                    break

                #left
                if 0 <= j-(k+1) < len(txt[i]) and txt[i][j-(k+1)] == '*':
                    if (i, j-(k+1)) in mult:
                        mult[(i,j-(k+1))] =  (int(num)* mult[(i, j-(k+1))][0],2)
                    else:
                        mult[(i, j-(k+1))] = (int(num), 1)
                    break

                #right
                if j+1 < len(txt[i]) and txt[i][j+1] == '*':
                    if (i, j+1) in mult:
                        mult[(i,j+1)] =  (int(num)* mult[(i, j+1)][0],2)
                    else:
                        mult[(i, j+1)] = (int(num), 1)
                    break

                #top left
                if 0 <= i-1 < len(txt) and 0 <= j-(k+1) < len(txt[i-1]) and txt[i-1][j-(k+1)] == '*':
                    if (i-1, j-(k+1)) in mult:
                        mult[(i-1,j-(k+1))] =  (int(num)* mult[(i-1, j-(k+1))][0],2)
                    else:
                        mult[(i-1, j-(k+1))] = (int(num), 1)
                    break

                #bottom left
                if 0 <= i+1 < len(txt) and 0 <= j-(k+1) < len(txt[i+1]) and txt[i+1][j-(k+1)] == '*':
                    if (i+1, j-(k+1)) in mult:
                        mult[(i+1,j-(k+1))] =  (int(num)* mult[(i+1, j-(k+1))][0],2)
                    else:
                        mult[(i+1, j-(k+1))] = (int(num), 1)
                    break

                #top right
                if 0 <= i-1 < len(txt) and j+1 < len(txt[i]) and txt[i-1][j+1] == '*':
                    if (i-1, j+1) in mult:
                        mult[(i-1,j+1)] =  (int(num)* mult[(i-1, j+1)][0],2)
                    else:
                        mult[(i-1, j+1)] = (int(num), 1)
                    break

                #bottom right
                if 0 <= i+1 < len(txt) and 0 <= j+1 < len(txt[i+1]) and txt[i+1][j+1] == '*':
                    if (i+1, j+1) in mult:
                        mult[(i+1,j+1)] =  (int(num)* mult[(i+1, j+1)][0],2)
                    else:
                        mult[(i+1, j+1)] = (int(num), 1)
                    break

                j += 1
        j += 1

for key in mult:
    if mult[key][1] == 2:
        sum += mult[key][0]
print("Sum:", sum)
