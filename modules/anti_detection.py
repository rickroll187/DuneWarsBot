import random
from config import SETTINGS, log

def should_skip_action():
    skip = random.random() < SETTINGS["SKIP_ACTION_PROBABILITY"]
    log.info(f"Anti-detection: {'Skipping' if skip else 'Proceeding'} (prob {SETTINGS['SKIP_ACTION_PROBABILITY']})")
    return skip

def random_delay():
    import time
    delay = random.uniform(*SETTINGS["ACTION_DELAY_RANGE"])
    log.info(f"Anti-detection: Sleeping for {delay:.2f}s")
    time.sleep(delay)
