import re
from sympy import solve, Symbol


### needed some linear algebra
def algebra(AX, AY, BX, BY, X, Y):
    a = Symbol("a", integer=True)
    b = Symbol("b", integer=True)
    X += 10000000000000
    Y += 10000000000000
    roots = solve(
        [a * AX + b * BX - X, a * AY + b * BY - Y],
        [a, b],
    )
    return roots[a] * 3 + roots[b] if roots else 0


with open("2024/13/input.txt")as f:
    ctn = f.read()
    entries = ctn.split("\n\n")
    equations = []
    for entry in entries:
        numbers = re.findall(r"\d+", "".join(entry))
        equations.append([int(d) for d in numbers])
res = 0
for equation in equations:
    res += algebra(*equation)
print(res)