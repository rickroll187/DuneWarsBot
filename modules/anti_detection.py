"""
Anti-Detection - Code Bros
Makes your bot blend in like it's one of the crowd.
"""
import random
from config import RANDOM_ACTION_ORDER, ACTION_DELAY_RANGE, SKIP_ACTION_PROBABILITY, log

def should_skip_action():
    """
    Randomly skip actions to look human.
    """
    skip = random.random() < SKIP_ACTION_PROBABILITY
    if skip:
        log("Should skip action? Yes (bot acting human).")
    else:
        log("Should skip action? Nah (bot flexing).")
    return skip

def random_delay():
    """
    Sleep for a random time to avoid bot detection.
    """
    delay = random.uniform(*ACTION_DELAY_RANGE)
    log(f"Sleeping for {delay:.2f}s to blend in.")
    time.sleep(delay)
