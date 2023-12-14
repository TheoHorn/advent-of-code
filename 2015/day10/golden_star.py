input = "1321131112"

def look_and_say(input):
    output = ""

    i = 0
    while i < len(input):
        count = 1
        while i + count < len(input) and input[i] == input[i + count]:
            count += 1
        output += str(count) + input[i]
        i += count
    
    return output

for i in range(50):
    input = look_and_say(input)
print(len(input))