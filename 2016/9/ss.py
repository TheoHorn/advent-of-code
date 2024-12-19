with open("2016/9/input.txt") as f:
    ctn = f.read().strip()

decompressed = ""
while ctn:
    current_carac = ctn[0]
    if ctn[0] == "(":
        marker_end = ctn.find(")")
        length, repetition = map(int, ctn[1:marker_end].split("x"))
        value = ctn[marker_end+1:marker_end+1+length]
        decompressed += value * repetition
        
        ctn = ctn[marker_end+1+length:]
    else:
        decompressed += ctn[0]
        ctn = ctn[1:]
print(len(decompressed))
    