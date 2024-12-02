import hashlib


res = "iwrupvqb"
bool = True
i = 0
while (bool):
    i = i + 1
    if hashlib.md5((res + str(i)).encode('utf-8')).hexdigest()[0:5] == "00000":
        print(i)
        bool = False