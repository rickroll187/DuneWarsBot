from config import SETTINGS, log
import random

def auto_battle(enemy):
    # Example logic: pick best troops, simulate outcome
    my_army = random.randint(800, 1500)
    enemy_army = enemy['army']
    outcome = "win" if my_army > enemy_army else "lose"
    loot = random.randint(1000, 7000) if outcome == "win" else 0
    log.info(f"[AutoBattle] Fought {enemy['name']} | My Army: {my_army} | Enemy Army: {enemy_army} | Outcome: {outcome} | Loot: {loot}")
    return {"enemy": enemy['name'], "my_army": my_army, "enemy_army": enemy_army, "outcome": outcome, "loot": loot}
