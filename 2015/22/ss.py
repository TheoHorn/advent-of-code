from collections import deque
from copy import deepcopy

with open("2015/22/input.txt") as f:
    lines = f.readlines()
    hp = int(lines[0].split(": ")[1])
    damage = int(lines[1].split(": ")[1])

boss = {"hp": hp, "damage": damage}
player = {"hp": 50, "armor": 0, "mana": 500, "shield": 0, "poison": 0, "recharge": 0}

spells = {
    "magic missile": {"cost": 53, "damage": 4, "heal": 0, "turns": 0, "armor": 0, "mana": 0},
    "drain": {"cost": 73, "damage": 2, "heal": 2, "turns": 0, "armor": 0, "mana": 0},
    "shield": {"cost": 113, "damage": 0, "heal": 0, "turns": 6, "armor": 7, "mana": 0},
    "poison": {"cost": 173, "damage": 3, "heal": 0, "turns": 6, "armor": 0, "mana": 0},
    "recharge": {"cost": 229, "damage": 0, "heal": 0, "turns": 5, "armor": 0, "mana": 101},
}

def apply_effects(player, boss):
    if player["shield"] > 0:
        player["armor"] = spells["shield"]["armor"]
        player["shield"] -= 1
    else:
        player["armor"] = 0

    if player["poison"] > 0:
        boss["hp"] -= spells["poison"]["damage"]
        player["poison"] -= 1

    if player["recharge"] > 0:
        player["mana"] += spells["recharge"]["mana"]
        player["recharge"] -= 1

def bfs(player, boss):
    queue = deque([(deepcopy(player), deepcopy(boss), 0, 0)])
    min_mana_spent = float('inf')
    visited = set()

    while queue:
        cur_player, cur_boss, mana_spent, turn = queue.popleft()

        if mana_spent >= min_mana_spent:
            continue

        apply_effects(cur_player, cur_boss)

        if cur_boss["hp"] <= 0:
            min_mana_spent = min(min_mana_spent, mana_spent)
            continue

        if cur_player["hp"] <= 0:
            continue

        state = (cur_player["hp"], cur_player["mana"], cur_player["shield"], cur_player["poison"], cur_player["recharge"], cur_boss["hp"], mana_spent, turn % 2)
        if state in visited:
            continue
        visited.add(state)

        if turn % 2 == 0:  # Player's turn
            for spell_name, spell in spells.items():
                if spell["cost"] > cur_player["mana"]:
                    continue

                if spell["turns"] > 0 and cur_player[spell_name] > 0:
                    continue

                new_player = deepcopy(cur_player)
                new_boss = deepcopy(cur_boss)
                new_mana_spent = mana_spent + spell["cost"]

                new_player["mana"] -= spell["cost"]

                if spell["turns"] > 0:
                    new_player[spell_name] = spell["turns"]
                else:
                    new_boss["hp"] -= spell["damage"]
                    new_player["hp"] += spell["heal"]

                queue.append((new_player, new_boss, new_mana_spent, turn + 1))
        else:  # Boss's turn
            damage = max(1, cur_boss["damage"] - cur_player["armor"])
            cur_player["hp"] -= damage
            queue.append((deepcopy(cur_player), deepcopy(cur_boss), mana_spent, turn + 1))

    return min_mana_spent

print(bfs(player, boss))
