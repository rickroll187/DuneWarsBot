import random
import time
from config import SETTINGS, log
from modules.anti_detection import should_skip_action, random_delay

def run(session, farm_amount):
    if not SETTINGS["AUTO_FARM"]:
        log.info("Banking skipped (AUTO_FARM off)")
        return
    if should_skip_action():
        log.info("Banking skipped (anti-detection)")
        return

    log.info(f"Banking {farm_amount} spice")
    # Simulate farm
    time.sleep(random.uniform(0.5, 1.5))
    random_delay()
    log.info(f"Farmed {farm_amount} spice")
