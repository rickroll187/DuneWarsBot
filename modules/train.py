import random
import time
from config import SETTINGS, log
from modules.anti_detection import should_skip_action, random_delay

def run(session, train_amount):
    if not SETTINGS["AUTO_TRAIN"]:
        log.info("Training skipped (AUTO_TRAIN off)")
        return
    if should_skip_action():
        log.info("Training skipped (anti-detection)")
        return

    log.info(f"Training {train_amount} units")
    time.sleep(random.uniform(0.5, 1.5))
    random_delay()
    log.info(f"Trained {train_amount} units")
