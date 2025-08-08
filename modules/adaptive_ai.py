from config import SETTINGS, log
import random

def adapt_strategy():
    # Example: change macro/priority based on spice or enemy threat
    spice = random.randint(0, 50000)
    if spice < 5000:
        SETTINGS["CUSTOM_MACROS"] = ["farm", "research", "repair"]
        log.info("[Adaptive AI] Low spice! Farming and repairing.")
    elif spice > 30000:
        SETTINGS["CUSTOM_MACROS"] = ["raid", "upgrade", "spy"]
        log.info("[Adaptive AI] Loaded! Time to raid and upgrade.")
    else:
        SETTINGS["CUSTOM_MACROS"] = ["train", "spy", "anti_covert"]
        log.info("[Adaptive AI] Balanced mode: training, spying, security.")
