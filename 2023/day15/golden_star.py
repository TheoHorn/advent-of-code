def algo_HASH(string):
    hash = 0
    for i in range(len(string)):
        hash += ord(string[i])
        hash *= 17
        hash = hash % 256
    return hash

with open("2023/day15/input.txt") as f:
    val = f.readline().split(",")

    list_box = [{} for i in range(256)]
    for string in val:
        if "=" in string:
            ope_index = string.index("=")
            name = string[:ope_index]
            box_number = algo_HASH(name)
        
            if name in list_box[box_number]:
                list_box[box_number].update({name: int(string[ope_index+1:])})
            else:
                list_box[box_number][name] = int(string[ope_index+1:])
        else:
            ope_index = string.index("-")
            name = string[:ope_index]
            box_number = algo_HASH(name)
            if name in list_box[box_number]:
                list_box[box_number].pop(name)
            else:
                continue

ans = 0
for i in range(len(list_box)):
    lb = list(list_box[i].values())
    for j in range(len(list_box[i])):
        ans += (i+1)*(j+1)*lb[j]
        print(ans)
print(ans)

        