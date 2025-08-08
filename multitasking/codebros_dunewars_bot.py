import threading
import yaml
import time
import random
import logging
from selenium.webdriver.common.by import By

# === Load Config ===
with open("codebros_config.yaml", "r") as f:
    CONFIG = yaml.safe_load(f)

MODE = CONFIG["mode"]
SPICE_BUFFER = CONFIG["spice_buffer"]
BANK_PARANOIA = CONFIG["bank_paranoia"]
DEFENSE_THRESHOLD = CONFIG["defense_threshold"]
REVENGE_MODE = CONFIG["revenge_mode"]
MAX_TRAIN_PER_CYCLE = CONFIG["max_train_per_cycle"]
STEALTH = CONFIG["stealth"]
ERROR_RETRIES = CONFIG["error_retries"]
LOG_FILE = CONFIG["log_file"]
DASHBOARD = CONFIG["dashboard"]

# === Set Up Logging ===
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
    format="[%(asctime)s] [Code Bros]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

def code_bros_log(msg):
    jokes = [
        "Running smoother than a spice harvester on nitro!",
        "If bots could dance, this would be a worm jig.",
        "Bro, even the Emperor is jealous of this multitasking.",
        "Sandworms can't keep up with these threads!",
        "Say hello to my little script!",
    ]
    joke = random.choice(jokes)
    print(f"[Code Bros] {msg} {joke}")
    logging.info(f"{msg} {joke}")

def stealth_wait(duration=None):
    if not STEALTH:
        time.sleep(duration or random.uniform(1, 2))
        return
    # Move mouse, scroll, random little delays
    sleep_time = duration or random.uniform(1.5, 3)
    for _ in range(random.randint(1, 3)):
        time.sleep(random.uniform(0.4, 1.1))
        # Placeholder for mouse move/scroll code
    time.sleep(sleep_time)

# === Shared State ===
shared_state = {
    "incoming_attacks": [],
    "stop": False,
}

# === Bot Tasks ===
def battlefield_task(driver):
    while not shared_state["stop"]:
        try:
            farm_or_raid(driver, MODE)
            code_bros_log("Battlefield: farming/raiding done!")
        except Exception as e:
            code_bros_log(f"Battlefield error: {e}")
        stealth_wait(random.uniform(30, 60))

def armoury_task(driver):
    while not shared_state["stop"]:
        try:
            dynamic_repair_weapons(driver, at_war=MODE in ["defending", "fighting"])
            auto_buy_weapons(driver, MODE)
            code_bros_log("Armoury: repairs and buys done!")
        except Exception as e:
            code_bros_log(f"Armoury error: {e}")
        stealth_wait(random.uniform(45, 90))

def training_task(driver):
    while not shared_state["stop"]:
        try:
            auto_train_units(driver, MODE)
            code_bros_log("Training: units trained!")
        except Exception as e:
            code_bros_log(f"Training error: {e}")
        stealth_wait(random.uniform(60, 120))

def bank_task(driver):
    while not shared_state["stop"]:
        try:
            # Withdraw if needed, otherwise deposit
            need_spice = 0
            fighting_onliner = any("online" in (atk.get("attacker", "").lower()) for atk in shared_state["incoming_attacks"])
            if fighting_onliner:
                need_spice = DEFENSE_THRESHOLD
            auto_manage_bank(driver, need_spice=need_spice, fighting_onliner=fighting_onliner)
            code_bros_log("Bank: managed like a pro accountant!")
        except Exception as e:
            code_bros_log(f"Bank error: {e}")
        stealth_wait(random.uniform(50, 100))

def mothership_task(driver):
    while not shared_state["stop"]:
        try:
            auto_manage_mothership(driver)
            code_bros_log("Mothership: upgraded and spicy!")
        except Exception as e:
            code_bros_log(f"Mothership error: {e}")
        stealth_wait(random.uniform(80, 150))

def logs_task(driver):
    while not shared_state["stop"]:
        try:
            incoming = scan_battle_logs(driver)
            shared_state["incoming_attacks"] = incoming
            # You can also call defense logic directly here if needed
            code_bros_log("Logs: battle logs scanned!")
        except Exception as e:
            code_bros_log(f"Logs error: {e}")
        stealth_wait(random.uniform(20, 60))

# === Main Entrypoint ===
def main(driver):
    threads = [
        threading.Thread(target=battlefield_task, args=(driver,)),
        threading.Thread(target=armoury_task, args=(driver,)),
        threading.Thread(target=training_task, args=(driver,)),
        threading.Thread(target=bank_task, args=(driver,)),
        threading.Thread(target=mothership_task, args=(driver,)),
        threading.Thread(target=logs_task, args=(driver,)),
    ]
    for t in threads:
        t.daemon = True
        t.start()
    code_bros_log("Code Bros MegaBot is live! All tasks running at once—no sandworm left unturned.")
    try:
        while True:
            stealth_wait(10)
    except KeyboardInterrupt:
        shared_state["stop"] = True
        code_bros_log("Code Bros MegaBot shutting down. Time to party!")

# Place your Selenium driver setup here and run:
# main(driver)