import re
from collections import Counter

with open("2016/4/input.txt") as f:
    lines = f.readlines()
    rooms = []
    for line in lines:
        match = re.match(r"([a-z-]+)-(\d+)\[[a-z]+\]", line.strip())
        if match:
            name, sector_id = match.groups()
            rooms.append((name, int(sector_id)))

for room in rooms:
    words = room[0].replace('-',' ')
    rotation = room[1] % 26
    decrypted_name = ''
    for char in words:
        if char != ' ':
            decrypted_char = chr((ord(char) - ord('a') + rotation) % 26 + ord('a'))
        else:
            decrypted_char = ' '
        decrypted_name += decrypted_char
    #print(f"Decrypted name: {decrypted_name}, Sector ID: {room[1]}")
    if 'northpole' in decrypted_name:
        print(f"Room with 'pole' in name: {decrypted_name}, Sector ID: {room[1]}")
