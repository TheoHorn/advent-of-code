def algo_HASH(string):
    hash = 0
    for i in range(len(string)):
        hash += ord(string[i])
        hash *= 17
        hash = hash % 256
    return hash

with open("2023/day15/input.txt") as f:
    val = f.readline().split(",")

    sum = 0
    for string in val:
        sum += algo_HASH(string)
    print(sum)