from config import SETTINGS, log
from modules import bank, combat, train, repair, upgrade, research, spy, anti_covert

ACTION_MAP = {
    "farm": lambda: bank.run(None, SETTINGS["FARM_AMOUNT"]),
    "raid": lambda: combat.run(None, SETTINGS["RAID_AMOUNT"], SETTINGS["RAID_MAX_TARGETS"]),
    "train": lambda: train.run(None, SETTINGS["TRAIN_AMOUNT"]),
    "repair": lambda: repair.run(None, SETTINGS["REPAIR_AMOUNT"]),
    "upgrade": lambda: upgrade.run(None, SETTINGS["UPGRADE_SPICE_THRESHOLD"]),
    "research": lambda: research.run(None),
    "spy": lambda: spy.run(None, SETTINGS["SPY_COUNT"], SETTINGS["SPY_MISSION"]),
    "anti_covert": lambda: anti_covert.run(None, SETTINGS["ANTICOVERT_SCAN_COUNT"], SETTINGS["ANTICOVERT_STRATEGY"]),
}

def run_macro(macro):
    log.info(f"Running custom macro: {macro}")
    for action in macro:
        if action in ACTION_MAP:
            ACTION_MAP[action]()
        else:
            log.info(f"Unknown macro action: {action}")
