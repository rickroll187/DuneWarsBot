from config import SETTINGS, log

def analyze_enemies():
    # Example: find weakest, strongest, likely targets
    enemies = SETTINGS["ENEMY_LIST"]
    weakest = min(enemies, key=lambda e: e['defense'])
    strongest = max(enemies, key=lambda e: e['army'])
    likely_attacker = max(enemies, key=lambda e: e['spies'])
    log.info(f"[Enemy Analysis] Weakest: {weakest['name']} | Strongest: {strongest['name']} | Likely Attacker: {likely_attacker['name']}")
    return {
        "weakest": weakest,
        "strongest": strongest,
        "likely_attacker": likely_attacker
    }
