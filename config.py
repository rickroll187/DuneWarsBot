# === Browser Settings ===
BROWSER = "chrome"
LOGIN_URL = "https://dunewars.net/login"
DASHBOARD_URL = "https://dunewars.net/base"

# === RAID Settings ===
ENABLE_RAID = True
RAID_MAX_TARGETS = 3
RAID_BLACKLIST_DURATION = 300  # in seconds (5 minutes)

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
