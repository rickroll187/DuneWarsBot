"""
Combat & Raiding - Code Bros
Smart target selection, blacklist, and spicy raid execution!
"""
import random
import time
from config import ENABLE_RAID, RAID_MAX_TARGETS, RAID_BLACKLIST_DURATION, log
from anti_detection import should_skip_action

# In-memory session blacklist (reset each run)
target_blacklist = {}

def fetch_targets(session):
    # TODO: Implement actual target scraping based on your game's HTML/API
    # This is a placeholder for demonstration.
    # Should return a list of dicts: [{'id': ..., 'army': ..., 'spice': ...}, ...]
    log("Fetching raid targets (placeholder)...")
    return [
        {'id': '123', 'army': 300, 'spice': 5000},
        {'id': '456', 'army': 500, 'spice': 7000},
        {'id': '789', 'army': 200, 'spice': 2000}
    ]

def raid_target(session, target):
    # TODO: Implement the actual raid POST request.
    log(f"Raiding target {target['id']} with {target['spice']} spice.")
    # Simulate success/failure
    success = random.random() > 0.25
    if not success:
        log(f"Raid on {target['id']} failed! Adding to blacklist.")
        target_blacklist[target['id']] = RAID_BLACKLIST_DURATION
    return success

def update_blacklist():
    # Decrement blacklist timers and remove expired
    for t in list(target_blacklist.keys()):
        target_blacklist[t] -= 1
        if target_blacklist[t] <= 0:
            del target_blacklist[t]

def run(session):
    if not ENABLE_RAID:
        log("Raiding disabled in config.")
        return
    log("Starting raid sequence!")
    update_blacklist()
    targets = fetch_targets(session)
    # Sort by most spice, filter blacklisted
    targets = [t for t in sorted(targets, key=lambda x: -x['spice']) if t['id'] not in target_blacklist]
    targets = targets[:RAID_MAX_TARGETS]
    for target in targets:
        if should_skip_action():
            log(f"Skipped raiding {target['id']} to look more human.")
            continue
        raid_target(session, target)
        time.sleep(random.uniform(2, 4))  # Extra realism
    log("Raid sequence finished.")