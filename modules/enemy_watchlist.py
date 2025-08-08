from config import SETTINGS, log

def alert_if_enemy_changes(new_stats):
    for enemy in new_stats:
        if enemy["name"] in SETTINGS["ENEMY_WATCHLIST"]:
            old_enemy = next((e for e in SETTINGS["ENEMY_LIST"] if e["name"] == enemy["name"]), None)
            if old_enemy and old_enemy != enemy:
                if SETTINGS["ENEMY_ALERTS_ENABLED"]:
                    log.info(f"[Alert] Watchlist enemy '{enemy['name']}' changed! New stats: Army={enemy['army']}, Defense={enemy['defense']}, Spice={enemy['spice']}, Spies={enemy['spies']}")
