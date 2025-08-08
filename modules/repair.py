import random
import time
from config import SETTINGS, log
from modules.anti_detection import should_skip_action, random_delay

def run(session, repair_amount):
    if not SETTINGS["AUTO_REPAIR"]:
        log.info("Repair skipped (AUTO_REPAIR off)")
        return
    if should_skip_action():
        log.info("Repair skipped (anti-detection)")
        return

    log.info(f"Repairing {repair_amount} units/weapons")
    time.sleep(random.uniform(0.5, 1.5))
    random_delay()
    log.info(f"Repaired {repair_amount} units/weapons")
