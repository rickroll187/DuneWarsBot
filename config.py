# === Browser/Game URLs ===
BROWSER = "chrome"
LOGIN_URL = "https://dunewars.net/login"
DASHBOARD_URL = "https://dunewars.net/base"

# === RAID SETTINGS ===
ENABLE_RAID = True
RAID_MAX_TARGETS = 3
RAID_BLACKLIST_DURATION = 300  # seconds

# === BANK SETTINGS ===
ENABLE_BANKING = True
BANK_MIN_BUFFER = 5000
BANK_SKIP_PROBABILITY = 0.1

# === REPAIR SETTINGS ===
ENABLE_REPAIR = True
REPAIR_RANDOMIZE = True
REPAIR_CRITICAL_THRESHOLD = 500
REPAIR_SKIP_PROBABILITY = 0.1

# === TRAIN SETTINGS ===
ENABLE_RETRAIN = True
RETRAIN_RANDOMIZE = True
RETRAIN_SKIP_PROBABILITY = 0.1

# === UPGRADE SETTINGS ===
ENABLE_AUTO_UPGRADE = True
UPGRADE_PRIORITY = ["defense", "economy", "infrastructure"]
UPGRADE_SPICE_THRESHOLD = 10000

# === RESEARCH SETTINGS ===
ENABLE_AUTO_RESEARCH = True
RESEARCH_PRIORITY = ["military", "economy", "infrastructure"]

# === ANTI-DETECTION SETTINGS ===
RANDOM_ACTION_ORDER = True
ACTION_DELAY_RANGE = (1.0, 3.0)  # seconds
SKIP_ACTION_PROBABILITY = 0.15

# === Logger ===
import logging
log = logging.getLogger("DuneWars")
log.setLevel(logging.DEBUG)
if not log.handlers:
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    log.addHandler(ch)
