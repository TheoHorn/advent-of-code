import re

with open("2016/7/input.txt") as f:
    lines = f.readlines()



def find_aba(segment):
    aba_patterns = []
    for i in range(len(segment) - 2):
        if segment[i] == segment[i + 2] and segment[i] != segment[i + 1]:
            aba_patterns.append(segment[i:i + 3])
    return aba_patterns


def has_bab(aba_patterns, segments_inside):
    for aba in aba_patterns:
        bab = aba[1] + aba[0] + aba[1]
        if any(bab in segment for segment in segments_inside):
            return True
    return False


ssl_count = 0
for line in lines:
    parts = re.split(r'\[|\]', line.strip())
    outside = parts[0::2] 
    inside = parts[1::2]   

    aba_patterns = []
    for segment in outside:
        aba_patterns.extend(find_aba(segment))

    if aba_patterns and has_bab(aba_patterns, inside):
        ssl_count += 1

print(ssl_count)
