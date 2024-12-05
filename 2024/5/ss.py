def verify(pages,dico):
    for i in range(len(pages)):
        key = pages[i]
        if key in dico:
            before = dico[key]
            j = 0
            for k in range(j,i):
                if pages[k] in before:
                    return False
    return True

with open("2024/5/input.txt") as f:
    content = f.read().strip()
    first_part = content.split("\n\n")[0]
    second_part = content.split("\n\n")[1]
    

    lines = first_part.split("\n")
    dico = {}
    for line in lines:
        key = int(line.split("|")[0])
        value = int(line.split("|")[1])
        if key in dico:
            tab = [value]
            old = dico[key]
            tab.extend(old)
            tab.sort(reverse=True)
            dico[key] = tab
        else:
            dico[key] = [value]
    
    summed = 0
    lines = second_part.split("\n")
    for line in lines : 
        pages = line.split(",")
        pages = [int(x) for x in pages]
        if (verify(pages,dico)):
            index = len(pages)//2
            summed += pages[index]
    print(summed)


