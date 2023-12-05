import copy


with open('2015/day8/input.txt') as f:
    list_hexa = []
    for i in range(0,256):
        list_hexa.append(hex(i)[2:].zfill(2))
    lines = f.read().splitlines()
    sum_chars = 0
    for line in lines:
        sum_chars += len(line)
    print(sum_chars)
    sum_chars_encoded = 0
    for line in lines:
        nl = copy.deepcopy(line)
        nl = nl.replace(R"\\","0")
        nl = nl.replace(R"\"","0")
        nl = nl.replace(R"\'","0")
        nl = nl.replace(R'"',"")
        if R"\x" in nl:
            for hexa in list_hexa:
                string = R"\x" + hexa
                nl = nl.replace(string,"0")
        print(nl)
        sum_chars_encoded += len(nl)
    print(sum_chars_encoded)

        
print(sum_chars - sum_chars_encoded)
                         
