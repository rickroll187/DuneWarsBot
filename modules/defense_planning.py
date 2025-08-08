from config import SETTINGS, log
import random

def plan_defense():
    # Example: upgrade defense if below threshold
    for enemy in SETTINGS["ENEMY_LIST"]:
        if enemy["army"] > SETTINGS["ENEMY_LIST"][0]["defense"]:
            log.info(f"[Defense] Upgrading defenses vs {enemy['name']}")
            # Simulate upgrade
            SETTINGS["ENEMY_LIST"][0]["defense"] += random.randint(100, 300)
        else:
            log.info(f"[Defense] Defense is strong against {enemy['name']}")
