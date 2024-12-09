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


start, end = 0, len(res) - 1

while start < end:
    # Find the next used block from the end
    while end >= 0 and res[end] == -1:
        end -= 1

    # Verify if start is too far
    if start >= end:
        break

    # Find file boundaries from the end
    file_end = end
    while file_end >= 0 and res[file_end] == res[end]:
        file_end -= 1
    
    file_length = end - file_end

    # Find the first gap large enough to hold the file (and not after the file)
    gap_start = None
    for i in range(start, end - file_length + 1): 
        if all(res[i + j] == -1 for j in range(file_length)):
            gap_start = i
            break
    
    if gap_start is not None:
        res[gap_start:gap_start + file_length] = res[file_end + 1:end + 1]
        res[file_end + 1:end + 1] = [-1] * file_length

        start = res.index(-1)
        end = file_end
    else:
        # Skip to the next file
        end = file_end

    # Debug output
    #print(res)
    #print(f"start: {start}, end: {end}")

ans = 0
for i,x in enumerate(res):
    if x != -1: ans += i*x
print(ans)