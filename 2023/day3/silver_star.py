f = open('day3/input.txt', 'r')
txt = f.read().split('\n')
sum = 0

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
                if 0 <= i-1 < len(txt) and 0 <= j-k < len(txt[i-1]) and txt[i-1][j-k] != '.' and txt[i-1][j-k] != '\n' and not txt[i-1][j-k].isdigit():
                    bool = True
                    print("top")

                #bottom
                if 0 <= i+1 < len(txt) and 0 <= j-k < len(txt[i+1]) and txt[i+1][j-k] != '.' and txt[i+1][j-k] != '\n' and not txt[i+1][j-k].isdigit():
                    bool = True
                    print("bottom")

                #left
                if 0 <= j-(k+1) < len(txt[i]) and txt[i][j-(k+1)] != '.' and txt[i][j-(k+1)] != '\n' and not txt[i][j-(k+1)].isdigit():
                    bool = True
                    print("left")

                #right
                if j+1 < len(txt[i]) and txt[i][j+1] != '.' and txt[i][j+1] != '\n' and not txt[i][j+1].isdigit():
                    bool = True
                    print("right")

                #top left
                if 0 <= i-1 < len(txt) and 0 <= j-(k+1) < len(txt[i-1]) and txt[i-1][j-(k+1)] != '.' and txt[i-1][j-(k+1)] != '\n' and not txt[i-1][j-(k+1)].isdigit():
                    bool = True
                    print("top left")

                #bottom left
                if 0 <= i+1 < len(txt) and 0 <= j-(k+1) < len(txt[i+1]) and txt[i+1][j-(k+1)] != '.' and txt[i+1][j-(k+1)] != '\n' and not txt[i+1][j-(k+1)].isdigit():
                    bool = True
                    print("bottom left")

                #top right
                if 0 <= i-1 < len(txt) and j+1 < len(txt[i]) and txt[i-1][j+1] != '.' and txt[i-1][j+1] != '\n' and not txt[i-1][j+1].isdigit():
                    bool = True
                    print("top right")

                #bottom right
                if 0 <= i+1 < len(txt) and 0 <= j+1 < len(txt[i+1]) and txt[i+1][j+1] != '.' and txt[i+1][j+1] != '\n' and not txt[i+1][j+1].isdigit():
                    bool = True
                    print("bottom right")

                j += 1
            if bool:
                print(num)
                sum += int(num)
        j += 1

print("Sum:", sum)
