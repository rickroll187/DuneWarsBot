import threading
import time
import random
from selenium.webdriver.common.by import By

def code_bros_log(msg):
    jokes = [
        "Multitasking harder than a mentat on spice!",
        "If sandworms had thumbs, they'd code like this.",
        "Bots wish they could keep up with Code Bros.",
        "Running all pages like a real Fremen.",
        "This bot's so smooth, even the Emperor's jealous.",
    ]
    print(f"[Code Bros] {msg} {random.choice(jokes)}")

def battlefield_task(driver):
    while True:
        farm_or_raid(driver, MODE)
        code_bros_log("Battlefield task complete!")
        time.sleep(random.uniform(30, 60))

def armoury_task(driver):
    while True:
        dynamic_repair_weapons(driver, at_war=MODE in ["defending", "fighting"])
        auto_buy_weapons(driver, MODE)
        code_bros_log("Armoury checked and fixed!")
        time.sleep(random.uniform(45, 90))

def training_task(driver):
    while True:
        auto_train_units(driver, MODE)
        code_bros_log("Training task completed!")
        time.sleep(random.uniform(60, 120))

def bank_task(driver):
    while True:
        # You can adjust need_spice/fighting_onliner based on shared info from logs
        auto_manage_bank(driver)
        code_bros_log("Bank managed like a spice accountant!")
        time.sleep(random.uniform(50, 100))

def mothership_task(driver):
    while True:
        auto_manage_mothership(driver)
        code_bros_log("Mothership upgraded and ready for warp!")
        time.sleep(random.uniform(80, 150))

def logs_task(driver, shared_state):
    while True:
        incoming = scan_battle_logs(driver)
        shared_state['incoming_attacks'] = incoming
        # Could also flag onliners, trigger defense, etc.
        code_bros_log("Battle logs scanned—ready for action!")
        time.sleep(random.uniform(20, 60))

def main(driver):
    shared_state = {'incoming_attacks': []}
    threads = [
        threading.Thread(target=battlefield_task, args=(driver,)),
        threading.Thread(target=armoury_task, args=(driver,)),
        threading.Thread(target=training_task, args=(driver,)),
        threading.Thread(target=bank_task, args=(driver,)),
        threading.Thread(target=mothership_task, args=(driver,)),
        threading.Thread(target=logs_task, args=(driver, shared_state)),
    ]
    for t in threads:
        t.daemon = True
        t.start()
    code_bros_log("Code Bros bot running on all cylinders. Sandworms can't keep up!")
    while True:
        time.sleep(10)  # Main thread just chills and cracks jokes

# Usage:
# main(driver)