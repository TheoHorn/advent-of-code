def decompress_length(data):
    """
    Recursively calculates the decompressed length of the data.
    """
    total_length = 0
    i = 0

    while i < len(data):
        if data[i] == "(":
            marker_end = data.find(")", i)
            length, repetition = map(int, data[i+1:marker_end].split("x"))

            # Calculate the length of the decompressed segment recursively
            segment = data[marker_end+1:marker_end+1+length]
            total_length += repetition * decompress_length(segment)

            i = marker_end + 1 + length
        else:
            total_length += 1
            i += 1

    return total_length

with open("2016/9/input.txt") as f:
    ctn = f.read().strip()

result = decompress_length(ctn)
print(result)
