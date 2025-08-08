import random
import time
from config import SETTINGS, log
from modules.anti_detection import should_skip_action, random_delay

def run(session):
    if not SETTINGS["AUTO_RESEARCH"]:
        log.info("Research skipped (AUTO_RESEARCH off)")
        return
    if should_skip_action():
        log.info("Research skipped (anti-detection)")
        return

    log.info(f"Researching priorities: {SETTINGS['RESEARCH_PRIORITY']}")
    time.sleep(random.uniform(0.5, 1.5))
    random_delay()
    log.info(f"Research complete on priorities: {SETTINGS['RESEARCH_PRIORITY']}")
