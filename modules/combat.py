import random
import time
from config import SETTINGS, log
from modules.anti_detection import should_skip_action, random_delay

target_blacklist = {}

def fetch_targets():
    # Simulate fetching targets
    return [
        {'id': '123', 'army': 300, 'spice': 5000},
        {'id': '456', 'army': 500, 'spice': 7000},
        {'id': '789', 'army': 200, 'spice': 2000}
    ]

def raid_target(target, raid_amount):
    log.info(f"Raiding target {target['id']} for {raid_amount} spice")
    success = random.random() > 0.25
    time.sleep(random.uniform(0.5, 1.5))
    random_delay()
    if not success:
        log.info(f"Raid on {target['id']} failed! Blacklisted.")
        target_blacklist[target['id']] = SETTINGS["RAID_BLACKLIST_DURATION"]
    else:
        log.info(f"Raid on {target['id']} successful!")
    return success

def update_blacklist():
    for t in list(target_blacklist.keys()):
        target_blacklist[t] -= 1
        if target_blacklist[t] <= 0:
            del target_blacklist[t]

def run(session, raid_amount, max_targets):
    if not SETTINGS["AUTO_RAID"]:
        log.info("Raiding skipped (AUTO_RAID off)")
        return
    update_blacklist()
    targets = [t for t in fetch_targets() if t['id'] not in target_blacklist]
    for target in targets[:max_targets]:
        if should_skip_action():
            log.info(f"Skipped raiding {target['id']} (anti-detection)")
            continue
        raid_target(target, raid_amount)
