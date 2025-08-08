import random
import time
from config import SETTINGS, log
from modules.anti_detection import should_skip_action, random_delay

def run(session, spice_threshold):
    if not SETTINGS["AUTO_UPGRADE"]:
        log.info("Upgrade skipped (AUTO_UPGRADE off)")
        return
    if should_skip_action():
        log.info("Upgrade skipped (anti-detection)")
        return

    log.info(f"Upgrading with threshold {spice_threshold} spice")
    time.sleep(random.uniform(0.5, 1.5))
    random_delay()
    log.info(f"Upgrade complete above threshold {spice_threshold} spice")
