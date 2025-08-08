"""
Research Module - Code Bros
Because knowledge is power (and sometimes, more spice).
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import random
import time
from config import ENABLE_AUTO_RESEARCH, RESEARCH_PRIORITY, log
from anti_detection import should_skip_action

def fetch_research_options(session):
    # TODO: Scrape available research topics and costs from the game's research page
    # Placeholder example:
    return [
        {"type": "economy", "level": 2, "cost": 6000, "id": "econ2"},
        {"type": "infrastructure", "level": 2, "cost": 7000, "id": "infra2"},
        {"type": "military", "level": 3, "cost": 10000, "id": "mil3"},
    ]

def fetch_spice_on_hand(session):
    # TODO: Scrape actual spice amount from empire/command center page
    return 20000

def perform_research(session, research):
    # TODO: Implement the actual research POST request
    log(f"Researching {research['type']} level {research['level']+1} for {research['cost']} spice.")
    time.sleep(random.uniform(1, 2))

def run(session):
    if not ENABLE_AUTO_RESEARCH:
        log("Auto-research skipped (disabled in config).")
        return
    if should_skip_action():
        log("Randomly skipped research for plausible deniability.")
        return

    spice = fetch_spice_on_hand(session)
    options = fetch_research_options(session)
    options = [r for r in options if r["cost"] <= spice]
    if not options:
        log("No affordable research topics available.")
        return
    for prio in RESEARCH_PRIORITY:
        for r in options:
            if r["type"] == prio:
                perform_research(session, r)
                log("Research complete. Knowledge is power, bro!")
                return
    log("No prioritized research available. Saving spice for next time.")
