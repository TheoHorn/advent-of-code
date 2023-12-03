


f = open('day3/input.txt', 'r')
txt = f.read().split('\n')
sum = 0
for i in range(len(txt)):
    j = 0
    while j < len(txt[i]):
        num = ''
        while j < len(txt[i]) and (txt[i][j] == '0' or txt[i][j] == '1' or txt[i][j] == '2' or txt[i][j] == '3' or txt[i][j] == '4' or txt[i][j] == '5' or txt[i][j] == '6' or txt[i][j] == '7' or txt[i][j] == '8' or txt[i][j] == '9'):
            num += txt[i][j]
            j += 1
            #print(num)
        bool = False
        for k in range(len(num)):
            if j-k < 0 or i-1 < 0 or j-k > len(txt[i-1]) or i-1 > len(txt):
                m = 0
            else : 
                if txt[i-1][j-k] != ('0' and '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9' and '.'and '\n'):
                    bool = True

            if j-k < 0 or i+1 >= len(txt):
                m = 0
            else:
                if txt[i+1][j-k] != ('0' and '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9' and '.'and '\n'):
                    bool = True
            if j-(k+1) < 0:
                m = 0
            else:
                if txt[i][j-(k+1)] != ('0' and '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9' and '.'and '\n'):
                    bool = True
            if j+1 >= len(txt[i]):
                m = 0
            else:
                if txt[i][j+1] != ('0' and '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9' and '.'and '\n'):
                    bool = True
            
            if i-1 < 0 or j-(k+1) < 0:
                m = 0
            else:
                if txt[i-1][j-(k+1)] != ('0' and '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9' and '.'and '\n'):
                    bool = True

            if i+1 >= len(txt) or j-(k+1) < 0:
                m = 0
            else:
                if txt[i+1][j-(k+1)] != ('0' and '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9' and '.'and '\n'):
                    bool = True

            if i-1 < 0 or j+1 >= len(txt[i]):
                m = 0
            else:
                if txt[i-1][j+1] != ('0' and '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9' and '.' and '\n'):
                    bool = True

            if i+1 >= len(txt) or j+1 >= len(txt[i]):
                m = 0
            else:
                if txt[i+1][j+1] != ('0' and '1' and '2' and '3' and '4' and '5' and '6' and '7' and '8' and '9' and '.'and '\n'):
                    bool = True


        if bool == True:
            print(num)
            sum += int(num)
        j += 1
        
            
        
