def to_bits(x):
    str_bin = bin(x)[2:]
    return str_bin.zfill(16)

def OR(x,y):
    x = int(x)
    y = int(y)
    x_bits = to_bits(x)
    y_bits = to_bits(y)
    result = ''
    for i in range(len(x_bits)):
        if x_bits[i] == '1' or y_bits[i] == '1':
            result += '1'
        else:
            result += '0'
    return int(result,2)

def AND(x,y):
    x = int(x)
    y = int(y)
    x_bits = to_bits(x)
    y_bits = to_bits(y)
    result = ''
    for i in range(len(x_bits)):
        if x_bits[i] == '1' and y_bits[i] == '1':
            result += '1'
        else:
            result += '0'
    return int(result,2)
    
def NOT(x):
    x = int(x)
    x_bits = to_bits(x)
    result = ''
    for i in range(len(x_bits)):
        if x_bits[i] == '1':
            result += '0'
        else:
            result += '1'
    return int(result,2)

def LSHIFT(x,y):
    x = int(x)
    y = int(y)
    x_bits = to_bits(x)
    result = x_bits[y:] + '0'*y
    return int(result,2)

def RSHIFT(x,y):
    x = int(x)
    y = int(y)
    x_bits = to_bits(x)
    result = '0'*y + x_bits[:-y]
    return int(result,2)