from time import perf_counter

def find_next(line):

    tab = []
    if line.count(0) == len(line):
        return 0
    else :
        for i in range(len(line)):
            if i+1 < len(line):
                tab.append(line[i+1] - line[i])
        val1 = line[-1]
        val2 = find_next(tab)
        #print(line,val1, val2)
        return val1 + val2


def test():
    start = perf_counter()

    
    somme = 0
    with open('2023/day9/input.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = list(map(int, line.split(' ')))
            line.reverse()
            #print(line)
            val = find_next(line)
            somme += val
    print(somme)

    stop = perf_counter()
    return stop-start

s = 0
for i in range(10000):
    s += test()
print(s/10000)