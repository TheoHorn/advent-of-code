import hashlib

with open("2016/5/input.txt") as f:
    password = f.read().strip()

index = 0
result = "........"

while "." in result:
    hash_input = f"{password}{index}".encode()
    hash_output = hashlib.md5(hash_input).hexdigest()
    if hash_output.startswith("00000"):
        if str.isdigit(hash_output[5]):
            position = int(hash_output[5])
            if 0 <= position <= 7:
                if result[position] == ".":
                    result = result[:position] + hash_output[6] + result[position+1:]
    index += 1

print(result)