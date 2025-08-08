"""
Anti-Detection & Humanization - Code Bros
Because getting banned is not part of the plan.
"""
import random
import time
from config import RANDOM_ACTION_ORDER, ACTION_DELAY_RANGE, SKIP_ACTION_PROBABILITY, log

def randomize_action_order(actions):
    if RANDOM_ACTION_ORDER:
        random.shuffle(actions)
        log("Action order randomized for extra stealth.")
    return actions

def maybe_delay():
    delay = random.uniform(*ACTION_DELAY_RANGE)
    log(f"Sleeping {delay:.2f} seconds to keep it spicy and human.")
    time.sleep(delay)

def should_skip_action():
    return random.random() < SKIP_ACTION_PROBABILITY