with open("2024/9/input.txt") as f:
    ctn = f.readline().strip()

ctn = list(map(int, ctn))
n = len(ctn)


res = []
for i, x in enumerate(ctn):
    if i % 2 == 0:  # Data block
        tab = [i//2] * x
    else:  # Useless block
        tab = [-1] * x
    res.extend(tab)

start, end = 1, len(res) - 1
while start < end:
    if res[start] == -1:
        if res[end] == -1:
            end -=1
        else:          
            res[start] = res[end]
            res[end] = -1
            end -= 1
            start += 1
    else:
        start += 1

x = res.index(-1)
res = res[:x]
ans = sum(i * x for i, x in enumerate(res))
print(ans)
