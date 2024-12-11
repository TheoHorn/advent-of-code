with open("2024/11/input.txt") as f:
    ctn = f.readline().split()

blinks = 25
numbers = ctn.copy()

for _ in range(blinks):
    new_numbers = []

    for val in numbers:
        if val.isdigit():
            num = int(val)
            if num == 0:
                new_numbers.append("1")
            elif len(val) % 2 == 0:
                half = len(val) // 2
                left = str(int(val[:half]))
                right = str(int(val[half:]))
                new_numbers.extend([left, right])
            else:
                new_numbers.append(str(num * 2024))
        else:
            new_numbers.append(val * 2024)

    numbers = new_numbers

print(len(numbers))
