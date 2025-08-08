from config import SETTINGS, log

def get_enemy_stats():
    if not SETTINGS.get("SHOW_ENEMY_STATS", True):
        log.info("Enemy stats display disabled.")
        return []
    return SETTINGS["ENEMY_LIST"]

def log_enemy_stats():
    enemies = get_enemy_stats()
    for enemy in enemies:
        log.info(
            f"Enemy '{enemy['name']}': Army={enemy['army']}, Defense={enemy['defense']}, Spice={enemy['spice']}, Spies={enemy['spies']}"
        )
