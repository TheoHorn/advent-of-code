import re
from itertools import product
with open("2023/19/input.txt") as f:
    lines = f.readlines()
    workflows = {}
    for i,line in enumerate(lines):
        if line == "\n":
            nexti = i+1
            break
        else:
            key_match = re.match(r"(\w+)\{(.+)\}", line)
            if key_match:
                key = key_match.group(1)
                rules_str = key_match.group(2)
                rules_list = rules_str.split(",")
                workflows[key] = rules_list
            else:
                print("Error")


ans = 0
for rating in product(range(1, 4001),repeat=4):
    current_point = "in" #
    while (current_point != "A" and current_point != "R"):
        rules = workflows[current_point]
        for rule in rules:
            if ":" in rule:
                terms = rule.split(":")
                condition = terms[0]
                next_point = terms[1]
                if ">" in condition:
                    cond = condition.split(">")
                    alpha_cond = cond[0]
                    value_cond = int(cond[1])
                    if alpha_cond == "x":
                        if rating[0] > value_cond:
                            current_point = next_point
                            break
                        else:
                            continue
                    elif alpha_cond == "m":
                        if rating[1] > value_cond:
                            current_point = next_point
                            break
                        else:
                            continue
                    elif alpha_cond == "a":
                        if rating[2] > value_cond:
                            current_point = next_point
                            break
                        else:
                            continue
                    else:
                        if rating[3] > value_cond:
                            current_point = next_point
                            break
                        else:
                            continue

                elif "<" in condition:
                    cond = condition.split("<")
                    alpha_cond = cond[0]
                    value_cond = int(cond[1])
                    if alpha_cond == "x":
                        if rating[0] < value_cond:
                            current_point = next_point
                            break
                        else:
                            continue
                    elif alpha_cond == "m":
                        if rating[1] < value_cond:
                            current_point = next_point
                            break
                        else:
                            continue
                    elif alpha_cond == "a":
                        if rating[2] < value_cond:
                            current_point = next_point
                            break
                        else:
                            continue
                    else:
                        if rating[3] < value_cond:
                            current_point = next_point
                            break
                        else:
                            continue
            else:
                current_point = rule
    if current_point == "A":
        ans += 1
print(ans)