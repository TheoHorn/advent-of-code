import re

with open("2024/3/input.txt") as f:
    content = f.read()
    data = []
    matches = re.split(r"(?<!\bdon't\(\)\b)do\(\)", content)
    for do in matches:
        dont_pos = do.find("don't()")
        if dont_pos != -1:
            do = do[:dont_pos]

        data.extend(re.findall(r"mul\((\d+),(\d+)\)", do))

    summed = sum(int(a) * int(b) for a, b in data)

    print(summed)   

                    
        

            
        