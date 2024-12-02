def lines_to_columns(lines):
    columns = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if j >= len(columns):
                columns.append(char)
            else:
                columns[j] += char
    return columns

def columns_to_lines(columns):
    lines = []
    for i, column in enumerate(columns):
        for j, char in enumerate(column):
            if j >= len(lines):
                lines.append(char)
            else:
                lines[j] += char
    return lines



def update_north(column):
    last_block = -1
    for j in range(len(column)):
        if column[j] == '#':
            last_block = j
        if column[j] == 'O':
            if j > last_block+1:
                column = column[:last_block+1] + 'O' + column[last_block + 2:]
                column = column[:j] + '.' + column[j + 1:]
                last_block +=1
            else:
                last_block = j
    return column

def update_south(column):
    last_block = len(column)
    for j in range(len(column)-1, -1, -1):
        if column[j] == '#':
            last_block = j
        if column[j] == 'O':
            if j < last_block-1:
                column = column[:j] + '.' + column[j + 1:]
                column = column[:last_block-1] + 'O' + column[last_block:]
                last_block -=1
            else:
                last_block = j
    return column

def lists_are_equal(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if list1[i][j] != list2[i][j]:
                return False
    return True

def count_weight(column):
    sum = 0
    length = len(column)
    for i in range(len(column)):
        if column[i] == 'O':
            sum += length - i
    return sum

def print_lines(lines):
    for line in lines:
        print(line)
    print()

with open("2023/day14/input.txt") as f:
    my_input = f.readlines()
    lines = [line.replace('\n', '') for line in my_input]
    boucle_trouve = False
    positions = []
    bool = True
    k=0
    #while bool:
    for i in range(155):
        positions.append(lines)
        
        columns = lines_to_columns(lines)
        for i in range(len(columns)):
            columns[i] = update_north(columns[i])
            
        lines = columns_to_lines(columns) 
        for i in range(len(lines)):
            lines[i] = update_north(lines[i])

        columns = lines_to_columns(lines)
        for i in range(len(columns)):
            columns[i] = update_south(columns[i])

        lines = columns_to_lines(columns)
        for i in range(len(lines)):
            lines[i] = update_south(lines[i])

        for i in range(len(positions)):
            if lists_are_equal(positions[i], lines):
                #print(i,k) #boulce -> 
                # 83 154
                #print_lines(positions[i])
                #print_lines(lines)
                bool = False

        k=k+1
    
    columns = lines_to_columns(lines)
    sum = 0
    for column in columns:
        sum += count_weight(column)
    print(sum)
