import hashlib

with open("2016/5/input.txt") as f:
    password = f.read().strip()

index = 0
result = ""

while len(result) < 8:
    hash_input = f"{password}{index}".encode()
    hash_output = hashlib.md5(hash_input).hexdigest()
    if hash_output.startswith("00000"):
        result += hash_output[5]
    index += 1

print(result)