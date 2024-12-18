import re
with open("2016/3/input.txt") as f:
    lines = f.readlines()
    triangles = []
    for line in lines:
        numbers = re.findall(r"\d+",line)
        triangles.append([int(numbers[0]), int(numbers[1]), int(numbers[2])])

valid_triangle = 0
for triangle in triangles:
    triangle = sorted(triangle,reverse=True)
    if triangle[0] < triangle[1] + triangle[2]:
        valid_triangle += 1
print(valid_triangle)