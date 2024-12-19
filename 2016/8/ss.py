array = [["." for _ in range(50)] for _ in range(6)]

with open("2016/8/input.txt") as f:
    lines = f.readlines()
    for line in lines:
        ctn = line.split()
        if ctn[0] == "rect":
            # Parse rectangle dimensions
            wide, tall = map(int, ctn[1].split('x'))
            for i in range(tall):
                for j in range(wide):
                    array[i][j] = "#"

        elif ctn[0] == "rotate" and "x" in ctn[2]:
            # Rotate column
            column = int(ctn[2].split('=')[1])
            shift = int(ctn[4])
            temp_col = [array[row][column] for row in range(len(array))]
            for row in range(len(array)):
                array[(row + shift) % len(array)][column] = temp_col[row]

        elif ctn[0] == "rotate" and "y" in ctn[2]:
            # Rotate row
            row = int(ctn[2].split('=')[1])
            shift = int(ctn[4])
            temp_row = array[row][:]
            for col in range(len(array[row])):
                array[row][(col + shift) % len(array[row])] = temp_row[col]

# Count the number of "#" symbols
count = sum(row.count("#") for row in array)

print(count)

