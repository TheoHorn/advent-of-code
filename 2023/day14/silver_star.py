def update_column(column):
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


def count_weight(column):
    sum = 0
    length = len(column)
    for i in range(len(column)):
        if column[i] == 'O':
            sum += length - i
    return sum

with open("2023/day14/input.txt") as f:
    my_input = f.readlines()
    columns = []
    for i, line in enumerate(my_input):
        for j, char in enumerate(line):
            if j >= len(columns):
                columns.append(char)
            else:
                columns[j] += char
    columns = columns[:-1]
    
    sum = 0
    for column in columns:
        column = update_column(column)
        print(column)
        sum += count_weight(column)
    print(sum)
