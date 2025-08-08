"""
Training Module - Code Bros
Keeps your troops swole (but not suspiciously so).
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import random
import time
from config import ENABLE_RETRAIN, RETRAIN_RANDOMIZE, RETRAIN_SKIP_PROBABILITY, log
from anti_detection import should_skip_action

def fetch_training_needs(session):
    # TODO: Scrape actual number of units needed from game's training page
    # Placeholder: return how many attack/defense specialists you can train
    return {'attack_needed': 20, 'defense_needed': 30}

def perform_training(session, att_amt, def_amt):
    # TODO: Implement the actual training POST request
    log(f"Training {att_amt} attack units & {def_amt} defense units.")
    time.sleep(random.uniform(1, 2))

def run(session):
    if not ENABLE_RETRAIN:
        log("Training skipped (disabled in config).")
        return
    if should_skip_action():
        log("Randomly skipped training for realism.")
        return

    needs = fetch_training_needs(session)
    att, deff = needs['attack_needed'], needs['defense_needed']

    if att + deff == 0:
        log("No training needed. Troops are already jacked.")
        return

    # Decide how many to train
    if not RETRAIN_RANDOMIZE:
        att_train, def_train = att, deff
        log("Full retrain mode: training all needed units.")
    else:
        att_train = int(att * random.uniform(0.5, 1.0))
        def_train = int(deff * random.uniform(0.5, 1.0))
        log(f"Partial retrain: {att_train} attack, {def_train} defense.")

    perform_training(session, att_train, def_train)
    log("Training routine complete.")
