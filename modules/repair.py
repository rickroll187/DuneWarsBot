"""
Repair Module - Code Bros
Dynamic partial repairs and human-like skipping!
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import random
import time
from config import ENABLE_REPAIR, REPAIR_RANDOMIZE, REPAIR_CRITICAL_THRESHOLD, REPAIR_SKIP_PROBABILITY, log
from anti_detection import should_skip_action

def fetch_damage_state(session):
    # TODO: Scrape the real damaged units from your game's repair page
    # Placeholder example:
    return {'att_damaged': 350, 'def_damaged': 620}

def perform_repair(session, att_amt, def_amt):
    # TODO: Implement the actual repair POST request
    log(f"Repairing {att_amt} attack units & {def_amt} defense units.")
    # Simulate repair time
    time.sleep(random.uniform(1, 2))

def run(session):
    if not ENABLE_REPAIR:
        log("Repair skipped (disabled in config).")
        return
    if should_skip_action():
        log("Randomly skipped repairs for stealth.")
        return

    damage = fetch_damage_state(session)
    att, deff = damage['att_damaged'], damage['def_damaged']

    if att + deff == 0:
        log("No repairs needed. All units fresh as a sandworm's bite.")
        return

    # Decide how much to repair
    if att + deff > REPAIR_CRITICAL_THRESHOLD or not REPAIR_RANDOMIZE:
        att_repair, def_repair = att, deff
        log("Critical damage detected or full repair mode: repairing everything.")
    else:
        att_repair = int(att * random.uniform(0.3, 0.8))
        def_repair = int(deff * random.uniform(0.3, 0.8))
        log(f"Partial repair: {att_repair} attack, {def_repair} defense.")

    perform_repair(session, att_repair, def_repair)
    log("Repair routine complete.")
