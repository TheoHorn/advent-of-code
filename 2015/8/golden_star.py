import copy


with open('2015/day8/input.txt') as f:
    list_hexa = []
    for i in range(0,256):
        list_hexa.append(hex(i)[2:].zfill(2))

    lines = f.read().splitlines()
    sum_chars = 0
    for line in lines:
        sum_chars += len(line)
    sum = 0
    for line in lines :
        nl = copy.deepcopy(line)
        nl = nl.replace(R"\\","0000")
        nl = nl.replace(R"\"","0000")
        nl = nl.replace(R"\'","0000")
        nl = nl.replace(R'"',"00")
        if R"\x" in nl:
            for hexa in list_hexa:
                string = R"\x" + hexa
                nl = nl.replace(string,"00000")
        sum = sum + len(nl) + 2

print(sum- sum_chars)

                         
