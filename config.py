import logging

# === Logger ===
log = logging.getLogger("DuneWars")
log.setLevel(logging.DEBUG)
if not log.handlers:
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    log.addHandler(ch)

# === Default Settings (UI can override these) ===
SETTINGS = {
    # General
    "BROWSER": "chrome",
    "LOGIN_URL": "https://dunewars.net/login",
    "DASHBOARD_URL": "https://dunewars.net/base",

    # Farming
    "AUTO_FARM": True,
    "FARM_AMOUNT": 10000,

    # Raiding
    "AUTO_RAID": True,
    "RAID_AMOUNT": 5000,
    "RAID_MAX_TARGETS": 3,
    "RAID_BLACKLIST_DURATION": 300,

    # Training
    "AUTO_TRAIN": True,
    "TRAIN_AMOUNT": 20,

    # Weapons Repair
    "AUTO_REPAIR": True,
    "REPAIR_AMOUNT": 500,

    # Upgrading
    "AUTO_UPGRADE": True,
    "UPGRADE_SPICE_THRESHOLD": 10000,
    "UPGRADE_PRIORITY": ["defense", "economy", "infrastructure"],

    # Research
    "AUTO_RESEARCH": True,
    "RESEARCH_PRIORITY": ["military", "economy", "infrastructure"],

    # Anti-detection
    "RANDOM_ACTION_ORDER": True,
    "ACTION_DELAY_RANGE": (1.0, 3.0),
    "SKIP_ACTION_PROBABILITY": 0.15,
}
