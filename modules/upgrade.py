"""
Upgrade Module - Code Bros
Spending spice on upgrades—'cause you can't take it with you!
"""
import random
import time
from config import ENABLE_AUTO_UPGRADE, UPGRADE_PRIORITY, UPGRADE_SPICE_THRESHOLD, log
from anti_detection import should_skip_action

def fetch_upgrade_options(session):
    # TODO: Scrape available upgrade options and costs from the game's upgrade page
    # Placeholder example:
    return [
        {"type": "economy", "level": 3, "cost": 8000},
        {"type": "infrastructure", "level": 2, "cost": 9000},
        {"type": "defense", "level": 4, "cost": 12000},
    ]

def fetch_spice_on_hand(session):
    # TODO: Scrape actual spice amount from empire/command center page
    return 20000

def perform_upgrade(session, upgrade):
    # TODO: Implement the actual upgrade POST request
    log(f"Upgrading {upgrade['type']} to level {upgrade['level']+1} for {upgrade['cost']} spice.")
    time.sleep(random.uniform(1, 2))

def run(session):
    if not ENABLE_AUTO_UPGRADE:
        log("Auto-upgrade skipped (disabled in config).")
        return
    if should_skip_action():
        log("Randomly skipped upgrades for stealth.")
        return

    spice = fetch_spice_on_hand(session)
    if spice < UPGRADE_SPICE_THRESHOLD:
        log(f"Not enough spice to upgrade (have {spice}, need at least {UPGRADE_SPICE_THRESHOLD}).")
        return

    options = fetch_upgrade_options(session)
    options = [u for u in options if u["cost"] <= spice]
    if not options:
        log("No affordable upgrades available!")
        return
    # Prioritize upgrades as per config
    for prio in UPGRADE_PRIORITY:
        for upg in options:
            if upg["type"] == prio:
                perform_upgrade(session, upg)
                log("Upgrade complete. Spice flows ever upward!")
                return
    log("No prioritized upgrades found. Holding onto spice for now.")