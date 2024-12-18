from collections import Counter
with open("2016/6/input.txt") as f:
    lines = f.readlines()
    c1, c2, c3, c4, c5, c6, c7, c8 = "", "", "", "", "", "", "", ""
    for line in lines:
        c1 += line[0]
        c2 += line[1]
        c3 += line[2]
        c4 += line[3]
        c5 += line[4]
        c6 += line[5]
        c7 += line[6]
        c8 += line[7]
        
counters = [Counter(c1), Counter(c2), Counter(c3), Counter(c4), Counter(c5), Counter(c6), Counter(c7), Counter(c8)]

most_common_values = [counter.most_common(1)[0][0] for counter in counters]
word = "".join(most_common_values)
print(word)