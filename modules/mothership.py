import time
import random

# Epic log history for dashboard
_log_history = []

def _epic_log(msg):
    jokes = [
        "Warp drives fixed—spice must flow faster!",
        "Mothership repairs: sandworms can't keep up!",
        "Upgraded the mothership—Emperor's jealous.",
        "If only it had a disco ball... maybe next upgrade.",
        "Code Bros mothership: more upgrades than a mentat on payday.",
        "If you love your mothership, put a repair bot on it!",
        "No one motherships like a Code Bro. Not even the Atreides.",
        "Can confirm: mothership shields stronger than my coffee.",
        "Upgrading so hard the Bene Gesserit are taking notes.",
        "Sandworms see our mothership and turn the other way.",
    ]
    full = f"{msg} {random.choice(jokes)}"
    print(f"[Mothership] {full}")
    _log_history.append(full)
    if len(_log_history) > 20:
        _log_history.pop(0)

def get_last_logs(n=8):
    return list(_log_history)[-n:]

def get_mothership_status(driver=None):
    # Replace with real scraping logic
    # Simulate status for demo
    repair_needed = random.random() < 0.22
    upgrade_ready = random.random() < 0.13
    hp = random.randint(6000, 10000)
    max_hp = 10000
    upgrade_cost = random.randint(800_000, 2_000_000)
    spice_on_hand = random.randint(500_000, 3_000_000)
    return {
        "needs_repair": repair_needed,
        "can_upgrade": upgrade_ready,
        "hp": hp,
        "max_hp": max_hp,
        "upgrade_cost": upgrade_cost,
        "spice_on_hand": spice_on_hand,
        "last_action": _log_history[-1] if _log_history else "",
        "last_logs": get_last_logs()
    }

def repair_mothership(driver=None):
    # Replace with real repair action
    time.sleep(random.uniform(0.5, 1.1))
    _epic_log("Mothership repaired to full HP, shields maxed out!")

def upgrade_mothership(driver=None):
    # Replace with real upgrade action
    time.sleep(random.uniform(1.0, 2.1))
    _epic_log("Mothership upgraded: new bling, new stings!")

def run(driver=None, **kwargs):
    """
    Main mothership maintenance runner. Respects dashboard custom args.
    """
    status = get_mothership_status(driver)
    hp_threshold = kwargs.get("hp_threshold", 8000)
    upgrade_spice = kwargs.get("upgrade_spice", 2_000_000)
    auto_upgrade = kwargs.get("auto_upgrade", True)
    auto_repair = kwargs.get("auto_repair", True)

    if auto_repair and status["hp"] < hp_threshold and status["needs_repair"]:
        _epic_log(f"HP at {status['hp']}/{status['max_hp']}. Repairs incoming!")
        repair_mothership(driver)
    elif status["needs_repair"]:
        _epic_log(f"HP at {status['hp']}/{status['max_hp']}. Repair needed, but auto-repair off.")
    else:
        _epic_log(f"HP at {status['hp']}/{status['max_hp']}. No repairs needed.")

    if auto_upgrade and status["can_upgrade"] and status["spice_on_hand"] >= status["upgrade_cost"] and status["spice_on_hand"] > upgrade_spice:
        _epic_log(f"Upgrade ready! Spice: {status['spice_on_hand']:,}, cost: {status['upgrade_cost']:,}.")
        upgrade_mothership(driver)
    elif status["can_upgrade"]:
        _epic_log(f"Upgrade ready, but not enough spice (have {status['spice_on_hand']:,}, need {upgrade_spice:,}).")
    else:
        _epic_log("No upgrade available right now.")

# Manual epic controls for dashboard
def manual_repair(driver=None):
    _epic_log("Manual repair button SMASHED!")
    repair_mothership(driver)

def manual_upgrade(driver=None):
    _epic_log("Manual upgrade button SLAPPED!")
    upgrade_mothership(driver)