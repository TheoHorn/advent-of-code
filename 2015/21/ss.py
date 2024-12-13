from itertools import combinations

with open("2015/21/input.txt") as f:
    lines = f.readlines()
    hp = int(lines[0].split(": ")[1])
    damage = int(lines[1].split(": ")[1])
    armor = int(lines[2].split(": ")[1])

boss = [hp,damage,armor]
player = [100,0,0]

def fight(player,boss):
    player_turn = True
    while (player[0] > 0 and boss[0] > 0):
        if player_turn:
            dmg = max(1, player[1] - boss[2])
            boss[0] -= dmg
        else:
            dmg = max(1, boss[1] - player[2])
            player[0] -= dmg
        player_turn = not player_turn
    if player[0] > 0:
        return True
    
shop = {"weapons":[[8,4,0],[10,5,0],[25,0,6],[40,7,0],[74,8,0]],"armors":[[0,0,0],[13,0,1],[31,0,2],[53,0,3],[75,0,4],[102,0,5]],"rings":[[0,0,0],[0,0,0],[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]}

least_cost = float("inf")
for weapon in shop["weapons"]:
    for armor in shop["armors"]:
        for rings in combinations(shop["rings"],2):
            cost = weapon[0]+armor[0]+rings[0][0]+rings[1][0]
            if cost > least_cost:
                continue
            else:
                player[1] = weapon[1] + rings[0][1] + rings[1][1]
                player[2] = armor[2] + rings[0][2] + rings[1][2]
                if fight(player[:], boss[:]):
                    most = cost
print(least_cost)
