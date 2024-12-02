def find_S(lines):
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == 'S':
                    return (i,j)

def update_grid(grid,letter):
    for i in range(len(letter)):
        for j in range(len(letter[i])):
            if letter[i][j] == '|':
                if i-1 >= 0 and i+1 < len(letter) and letter[i-1][j] in ['|','7','F','S'] and letter[i+1][j] in ['|','L','J','S']:
                    grid[i][j] = -1
            if letter[i][j] == '-':
                if j-1 >= 0 and j+1 < len(letter[i]) and letter[i][j-1] in ['-','F','L','S'] and letter[i][j+1] in ['-','7','J','S']:
                    grid[i][j] = -1
            if letter[i][j] == '7':
                if j-1 >= 0 and i+1 < len(letter) and letter[i][j-1] in ['-','F','L','S'] and letter[i+1][j] in ['|','L','J','S']:
                    grid[i][j] = -1
            if letter[i][j] == 'J':
                if j-1 >= 0 and i-1 >= 0 and letter[i][j-1] in ['-','L','F','S'] and letter[i-1][j] in ['|','7','F','S']:
                    grid[i][j] = -1
            if letter[i][j] == 'F':
                if i+1 < len(letter) and j+1 < len(letter[i]) and letter[i][j+1] in ['-','7','J','S'] and letter[i+1][j] in ['|','L','J','S']:
                    grid[i][j] = -1
            if letter[i][j] == 'L':
                if i-1 >= 0 and j+1 < len(letter[i]) and letter[i][j+1] in ['-','7','J','S'] and letter[i-1][j] in ['|','7','F','S']:
                    grid[i][j] = -1
            if letter[i][j] == '.':
                grid[i][j] = -8 
    return grid
                
def find_path(grid,letter):
    for k in range(1,10000):
        for i in range(len(letter)):
            for j in range(len(letter[i])):
                if grid[i][j] >= -1 :
                    if i-1 >= 0 and grid[i-1][j] >= 0 and letter[i-1][j] in ['|','7','F','S'] and letter[i][j] in ['|','L','J','S']:
                        grid[i][j] = grid[i-1][j] + 1
                    elif i+1 < len(letter) and grid[i+1][j] >= 0 and letter[i+1][j] in ['|','L','J','S'] and letter[i][j] in ['|','7','F','S']:
                        grid[i][j] = grid[i+1][j] + 1
                    elif j-1 >= 0 and grid[i][j-1] >= 0 and letter[i][j-1] in ['-','F','L','S'] and letter[i][j] in ['-','7','J','S']:
                        grid[i][j] = grid[i][j-1] + 1
                    elif j+1 < len(letter[i]) and grid[i][j+1] >= 0 and letter[i][j+1] in ['-','7','J','S'] and letter[i][j] in ['-','F','L','S']:
                        grid[i][j] = grid[i][j+1] + 1                
    return grid      

def rebuild_path(grid,letter):
    new_grid = [['' for j in range(len(letter[0]))] for i in range(len(letter))]
    for i in range(len(letter)):
        for j in range(len(letter[i])):
            if grid[i][j] >= 0:
                new_grid[i][j] = letter[i][j]
            else:
                new_grid[i][j] = '.'
    for i in range(len(letter)):
        for j in range(len(letter[i])):
            new_grid[i][j] = new_grid[i][j].replace('|', '│')
            new_grid[i][j] = new_grid[i][j].replace('-', '─')
            new_grid[i][j] = new_grid[i][j].replace('F', '┌')
            new_grid[i][j] = new_grid[i][j].replace('L', '└')
            new_grid[i][j] = new_grid[i][j].replace('7', '┐')
            new_grid[i][j] = new_grid[i][j].replace('J', '┘')
    return new_grid


with open('2023/day10/input.txt') as f:
    lines = f.read().split('\n')
    letter = [[j for j in line] for line in lines]
    i_s,j_s = find_S(letter)
    grid = [[-8 for j in range(len(letter[0]))] for i in range(len(letter))]
    grid[i_s][j_s] = 0
    grid = update_grid(grid,letter)
    grid = find_path(grid,letter)
    grid = rebuild_path(grid,letter)

with open('2023/day10/output2.txt', 'a') as f:
    f.write('Golden star - 2023/day10\n')
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            f.write(grid[i][j])
        f.write('\n')

    