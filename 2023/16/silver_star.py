def light_ray(x,y,dir,grid, list_of_visited):
    boolean = True
    maybe_cycle = False
    while boolean:
        if x < 0 or y < 0 or x > len(grid)-1 or y > len(grid[0])-1:
            return list_of_visited
        
        if maybe_cycle:
            if (x,y) in list_of_visited:
                return list_of_visited
            else:
                maybe_cycle = False
                list_of_visited.append((x,y,dir))
        if (x,y) in list_of_visited:
            maybe_cycle = True
        else:
            list_of_visited.append((x,y,dir))            


        if dir == "0":
            if grid[x][y] == "/":
                dir = "1"
                x -= 1
            elif grid[x][y] == "\\":
                dir = "3"
                x += 1
            elif grid[x][y] == "|":
                list_of_visited.extend(light_ray(x+1,y,"3",grid, list_of_visited))
                dir = "1"
                x -= 1
            else:
                y += 1

        elif dir == "1":
            if grid[x][y] == "/":
                dir = "0"
                y += 1
            elif grid[x][y] == "\\":
                dir = "2"
                y -= 1
            elif grid[x][y] == "-":
                list_of_visited.extend(light_ray(x,y-1,"2",grid, list_of_visited))
                dir = "0"
                y += 1
            else:
                x -= 1

        elif dir == "2":
            if grid[x][y] == "/":
                dir = "3"
                x += 1
            elif grid[x][y] == "\\":
                dir = "1"
                x -= 1
            elif grid[x][y] == "|":
                list_of_visited.extend(light_ray(x-1,y,"1",grid, list_of_visited))
                dir = "3"
                x += 1
            else:
                y -= 1
        
        elif dir == "3":
            if grid[x][y] == "/":
                dir = "2"
                y -= 1
            elif grid[x][y] == "\\":
                dir = "0"
                y += 1
            elif grid[x][y] == "-":
                list_of_visited.extend(light_ray(x,y+1,"0",grid, list_of_visited))
                dir = "2"
                y -= 1
            else:
                x += 1     

import sys
sys.setrecursionlimit(100)

with open("2023/day16/input.txt") as f:
    data = f.read().split("\n")
    print(len(light_ray(0,0,"0",data,[])))
    
