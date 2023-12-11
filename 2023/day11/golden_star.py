def length_btw_galaxies(stars, line_empty, column_empty, dist_btw_galaxies):
    ans = 0
    marqued = []
    for i in range(len(stars)):
        marqued.append(stars[i])
        for j in range(i + 1, len(stars)):
            if stars[j] in marqued:
                continue
            else:
                dist_x = 0
                dist_y = 0
                for k in range(min(stars[i][0], stars[j][0]), max(stars[i][0], stars[j][0])):
                    if k in line_empty:
                        dist_x += dist_btw_galaxies - 1
                    dist_x += 1
                for k in range(min(stars[i][1], stars[j][1]), max(stars[i][1], stars[j][1])):
                    if k in column_empty:
                        dist_y += dist_btw_galaxies - 1
                    dist_y += 1
                ans += dist_x + dist_y
    return ans

with open ('2023/day11/input.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    line_empty = []
    column_empty = []
    for i, line in enumerate(lines):
        if line.find('#') == -1:
            line_empty.append(i)
    
    for i in range(len(lines[0])):
        column = ''
        col = column.join([line[i] for line in lines])
        if col.find('#') == -1:
            column_empty.append(i)

    stars = []
    for i, line in enumerate(lines):
        offset = 0
        while line:
            if line.find('#', offset) != -1:
                stars.append((i, line.find('#', offset)))
                offset = line.find('#', offset) + 1
            else:
                break
    
print(length_btw_galaxies(stars, line_empty, column_empty, 1000000))
    


    