"""
Banking Module - Code Bros
Protects your spice like it's grandma's secret cookie recipe.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import random
import time
from config import ENABLE_BANKING, BANK_MIN_BUFFER, BANK_SKIP_PROBABILITY, log
from anti_detection import should_skip_action

def fetch_spice_on_hand(session):
    # TODO: Scrape actual spice amount from your empire/command center page
    # Placeholder for demo
    return 20000

def perform_banking(session, amount):
    # TODO: Implement the actual banking POST request
    log(f"Banking {amount} spice to keep it safe from sandworms (and other players).")
    time.sleep(random.uniform(1, 2))

def run(session):
    if not ENABLE_BANKING:
        log("Banking skipped (disabled in config).")
        return
    if should_skip_action() or random.random() < BANK_SKIP_PROBABILITY:
        log("Randomly skipped banking for realism.")
        return

    spice = fetch_spice_on_hand(session)
    to_bank = spice - BANK_MIN_BUFFER
    if to_bank <= 0:
        log("Not enough spice to bank. Holding for now.")
        return

    perform_banking(session, to_bank)
    log(f"Banked {to_bank} spice, left {BANK_MIN_BUFFER} out for emergencies (or flexing).")
