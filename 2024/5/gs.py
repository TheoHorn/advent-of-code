import copy

def verify(pages, dico):
    for i in range(len(pages)):
        key = pages[i]
        if key in dico:
            before = dico[key]
            for k in range(i):
                if pages[k] in before:
                    return False
    return True

def correct_ordering(pages, dico): 
    new_pages = pages[:]
    for i in range(len(pages)):
        key = pages[i]
        if key in dico:
            before = dico[key]
            for k in range(i):
                if new_pages[k] in before:
                    # Swap elements to correct order
                    new_pages[k], new_pages[i] = new_pages[i], new_pages[k]
                    break
    return new_pages

with open("2024/5/input.txt") as f:
    content = f.read().strip()
    first_part, second_part = content.split("\n\n")

    lines = first_part.split("\n")
    dico = {}
    for line in lines:
        key, value = map(int, line.split("|"))
        if key in dico:
            dico[key].append(value)
            dico[key].sort(reverse=True)
        else:
            dico[key] = [value]

    summed = 0
    lines = second_part.split("\n")
    for line in lines:
        pages = list(map(int, line.split(",")))
        if not verify(pages, dico):  
            while not verify(pages, dico):
                pages = correct_ordering(pages, dico)
            index = len(pages) // 2
            summed += pages[index] 

    print(summed)
