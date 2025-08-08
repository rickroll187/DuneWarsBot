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

# === MONSTER BOT SETTINGS ===
SETTINGS = {
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

    # Repair
    "AUTO_REPAIR": True,
    "REPAIR_AMOUNT": 500,

    # Upgrade
    "AUTO_UPGRADE": True,
    "UPGRADE_SPICE_THRESHOLD": 10000,
    "UPGRADE_PRIORITY": ["defense", "economy", "infrastructure"],

    # Research
    "AUTO_RESEARCH": True,
    "RESEARCH_PRIORITY": ["military", "economy", "infrastructure"],

    # Spy Network
    "AUTO_SPY": True,
    "SPY_COUNT": 5,
    "SPY_MISSION": "intel",  # 'scout', 'sabotage', 'intel'

    # Anti-Covert Ops
    "AUTO_ANTICOVERT": True,
    "ANTICOVERT_SCAN_COUNT": 3,
    "ANTICOVERT_STRATEGY": "scan",  # 'scan', 'trap', 'counter-intel'

    # Enemy Stats
    "SHOW_ENEMY_STATS": True,
    "ENEMY_LIST": [
        {"name": "BaronHarkonnen", "army": 1200, "defense": 800, "spice": 50000, "spies": 2},
        {"name": "FremenLegend", "army": 900, "defense": 950, "spice": 42000, "spies": 3},
        {"name": "GuildNavigator", "army": 650, "defense": 1000, "spice": 32000, "spies": 1},
    ],

    # Anti-detection
    "RANDOM_ACTION_ORDER": True,
    "ACTION_DELAY_RANGE": (1.0, 3.0),
    "SKIP_ACTION_PROBABILITY": 0.15,

    # Dashboard
    "MAX_LOG_LINES": 100,

    # === Battle Reports ===
    "ENABLE_BATTLE_REPORTS": True,
    "BATTLE_HISTORY": [],

    # === Custom Actions ===
    "CUSTOM_MACROS": [],  # Example: ["raid", "spy", "upgrade"]

    # === Resource Management ===
    "RESOURCE_AUTOBANK": True,
    "RESOURCE_AUTOSPEND": True,
    "RESOURCE_AUTOSAVE_THRESHOLD": 20000, # Minimum spice/gold to save

    # === Enemy Watchlist ===
    "ENEMY_WATCHLIST": ["BaronHarkonnen"],
    "ENEMY_ALERTS_ENABLED": True,

    # === Stats Graphs/Charts ===
    "ENABLE_STATS_GRAPHS": True,
    "STATS_HISTORY": [],
}
