def light_ray(x,y,dir,grid):
    boolean = True
    maybe_cycle = False
    list_of_visited = []
    list_light = []
    first_light = [x,y,dir]
    list_light.append(first_light)
    k = 0
    while k < len(list_light):
        light = list_light[k]
        while boolean:
            if light[0] < 0 or light[1] < 0 or light[0] > len(grid)-1 or light[1] > len(grid[0])-1:
                break
            
            if maybe_cycle:
                if (light[0],light[1],light[2]) in list_of_visited:
                    break
                else:
                    maybe_cycle = False
                    list_of_visited.append(light)
            if (light[0],light[1],light[2]) in list_of_visited:
                maybe_cycle = True
            else:
                new_place = (light[0],light[1],light[2])
                list_of_visited.append(new_place)            


            if light[2]== "0":
                if grid[light[0]][light[1]] == "/":
                    light[2]= "1"
                    light[0] -= 1
                elif grid[light[0]][light[1]] == "\\":
                    light[2]= "3"
                    light[0] += 1
                elif grid[light[0]][light[1]] == "|":
                    if light[0]+1 < len(grid):
                        n_light = [light[0]+1,light[1],"3"]
                        if n_light not in list_light:
                            list_light.append(n_light)
                    light[2]= "1"
                    light[0] -= 1
                else:
                    light[1] += 1

            elif light[2]== "1":
                if grid[light[0]][light[1]] == "/":
                    light[2]= "0"
                    light[1] += 1
                elif grid[light[0]][light[1]] == "\\":
                    light[2]= "2"
                    light[1] -= 1
                elif grid[light[0]][light[1]] == "-":
                    if light[1]-1 >= 0:
                        n_light = [light[0],light[1]-1,"2"]
                        if n_light not in list_light:
                            list_light.append(n_light)
                    
                    light[2]= "0"
                    light[1] += 1
                else:
                    light[0] -= 1

            elif light[2]== "2":
                if grid[light[0]][light[1]] == "/":
                    light[2]= "3"
                    light[0] += 1
                elif grid[light[0]][light[1]] == "\\":
                    light[2]= "1"
                    light[0] -= 1
                elif grid[light[0]][light[1]] == "|":
                    if light[0]-1 >= 0:
                        n_light = [light[0]-1,light[1],"1"]
                        if n_light not in list_light:
                            list_light.append(n_light)
                    light[2]= "3"
                    light[0] += 1
                else:
                    light[1] -= 1
            
            elif light[2]== "3":
                if grid[light[0]][light[1]] == "/":
                    light[2]= "2"
                    light[1] -= 1
                elif grid[light[0]][light[1]] == "\\":
                    light[2]= "0"
                    light[1] += 1
                elif grid[light[0]][light[1]] == "-":
                    if light[1]+1 < len(grid[0]):
                        n_light = [light[0],light[1]+1,"0"]
                        if n_light not in list_light:
                            list_light.append(n_light)
                    light[2]= "2"
                    light[1] -= 1
                else:
                    light[0] += 1 
        k += 1  
    visited = {} 
    for i in list_of_visited:
        if i[0] < 0 or i[1] < 0 or i[0] > len(grid)-1 or i[1] > len(grid[0])-1:
            continue
        visited.update({(i[0],i[1]):i[2]})
    l = list(visited.keys())
    l.sort()
    #print(l)
    return visited


with open("2023/day16/input.txt") as f:
    data = f.read().split("\n")
    maxi = 0
    for i in range(len(data)):
        maxi = max(maxi, len(light_ray(i,0,"0",data)))
        maxi = max(maxi, len(light_ray(i,len(data[0])-1,"2",data)))
        maxi = max(maxi, len(light_ray(0,i,"3",data)))
        maxi = max(maxi, len(light_ray(len(data)-1,i,"1",data)))
    print(maxi)
            
    
