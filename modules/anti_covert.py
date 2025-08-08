import random
import time
from config import SETTINGS, log
from modules.anti_detection import should_skip_action, random_delay

ANTICOVERT_STRATEGIES = {
    "scan": "Scanning for enemy spies",
    "trap": "Setting traps for infiltrators",
    "counter-intel": "Running counter-intelligence ops"
}

def run(session, scan_count, strategy):
    if not SETTINGS["AUTO_ANTICOVERT"]:
        log.info("Anti-Covert ops skipped (AUTO_ANTICOVERT off)")
        return
    if should_skip_action():
        log.info("Anti-Covert action skipped (anti-detection)")
        return

    strat_desc = ANTICOVERT_STRATEGIES.get(strategy, "Unknown strategy")
    for i in range(scan_count):
        log.info(f"Anti-Covert #{i+1}: {strat_desc}")
        time.sleep(random.uniform(0.2, 0.5))
        random_delay()
        # Simulate success/failure
        found = random.random() > 0.5
        if found:
            log.info(f"Anti-Covert #{i+1}: Enemy spy CAUGHT! Security flex.")
        else:
            log.info(f"Anti-Covert #{i+1}: No infiltrators found (keep scanning!)")
