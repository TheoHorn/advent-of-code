from itertools import permutations

numpad = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
                 "0": (3, 1), "A": (3, 2),
}

direcpad = {
                 "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2),
}  

def find_path(path, depth, keypad_bool, current=None):
    if not path:
        return 0

    # Select the appropriate keypad 
    if keypad_bool:
        keypad = direcpad
    else:
        keypad = numpad

    # Determine the current position
    if current:
        row, col = current 
    else:
        row,col = keypad["A"]

    target_row, target_col = keypad[path[0]]
    row_diff, col_diff = target_row - row, target_col - col
    moves = ""

    if row_diff > 0:
        moves += "v" * row_diff
    else:
        moves += "^" * (-row_diff)
    
    if col_diff > 0:
        moves += ">" * col_diff
    else:
        moves += "<" * (-col_diff)

    if depth == 0:
        return (len(moves) + 1 + find_path(path[1:], depth, keypad_bool, (target_row, target_col)))

    candidates = []
    # Look for permutations to find the shortest path 
    # ex : >>^ and ^>>, one can be shorter in an other depth
    for permutation in set(permutations(moves)):
        row, col = current or keypad["A"]

        directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}  
        for move in permutation:
            row_diff, col_diff = directions[move]
            row, col = row + row_diff, col + col_diff

            if (row, col) not in keypad.values():
                break
        else:
            candidates.append(find_path("".join(permutation) + "A", depth - 1, True))

    min_len = min(candidates) if candidates else -1

    return min_len + find_path(path[1:], depth, keypad_bool, (target_row, target_col))

with open("2024/21/input.txt") as f:
    ctn = f.readlines()
    codes = []
    for code in ctn:
        codes.append(code.strip())

result = 0

for code in codes:
    val = int("".join(c for c in code if c.isdigit()))
    sequence_length = find_path(code,2,False)
    result += val * sequence_length

print(result)