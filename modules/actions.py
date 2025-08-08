import random
import time
from config import BASE_URL, ACTION_DELAY_RANGE, log
from scraper import get_untrained, get_antibot_token, get_repair_status

def delay_action():
    t = random.uniform(*ACTION_DELAY_RANGE)
    log(f"Sleeping for {t:.2f} seconds to look human.")
    time.sleep(t)

def deposit_to_bank(session, spice, min_buffer, bank_space_left=None):
    amount = max(0, spice - min_buffer)
    if bank_space_left is not None:
        amount = min(amount, bank_space_left)
    if amount > 0:
        try:
            r = session.post(f"{BASE_URL}/bank/into", data={"amountB": amount, "Deposit": "Deposit"})
            log(f"Deposited {amount} spice to the bank. Response code: {r.status_code}")
        except Exception as e:
            log(f"Bank deposit failed: {e}")
        delay_action()
    else:
        log("No excess spice to deposit.")

def retrain(session, train_html):
    untrained = get_untrained(train_html)
    if untrained < 1:
        log("No untrained soldiers to retrain.")
        return
    # Sometimes retrain all, sometimes partial, sometimes none
    roll = random.random()
    if roll < 0.25:
        train_amt = 0
        log("Skipping retrain this cycle for realism.")
    elif roll < 0.75:
        train_amt = random.randint(1, untrained)
        log(f"Retraining a partial batch: {train_amt} out of {untrained} untrained.")
    else:
        train_amt = untrained
        log(f"Retraining all {untrained} untrained soldiers.")
    if train_amt < 1:
        return
    half = train_amt // 2
    antibot_token = get_antibot_token(train_html)
    try:
        r = session.post(f"{BASE_URL}/train/train", data={
            "miner": 0,
            "atsold": half,
            "defsold": train_amt - half,
            "satsold": 0,
            "sdefsold": 0,
            "spy": 0,
            "spykiller": 0,
            "time1t": antibot_token,
            "train": "Train Units"
        })
        log(f"Retrained {train_amt} soldiers. Response code: {r.status_code}")
    except Exception as e:
        log(f"Retrain failed: {e}")
    delay_action()

def dynamic_repair_all(session, repair_html):
    status = get_repair_status(repair_html)
    att_damage = status.get("att_damaged", 0)
    def_damage = status.get("def_damaged", 0)
    # Decide repair behavior
    roll = random.random()
    att_repair = 0
    def_repair = 0
    # Always repair if very damaged
    if att_damage + def_damage > 1000 or roll < 0.2:
        att_repair = att_damage
        def_repair = def_damage
        log(f"Repairing ALL damaged: att {att_repair}, def {def_repair}")
    elif roll < 0.7:
        att_repair = int(att_damage * random.uniform(0.2, 0.7))
        def_repair = int(def_damage * random.uniform(0.2, 0.7))
        log(f"Repairing PARTIAL units: att {att_repair}, def {def_repair}")
    else:
        log("Skipping repairs this cycle.")
    # Only send repair requests if anything to repair
    if att_repair > 0:
        try:
            session.post(f"{BASE_URL}/armoury/repair", data={'att_repair_amount': att_repair})
        except Exception as e:
            log(f"Attack repair failed: {e}")
    if def_repair > 0:
        try:
            session.post(f"{BASE_URL}/armoury/repair", data={'def_repair_amount': def_repair})
        except Exception as e:
            log(f"Defense repair failed: {e}")
    delay_action()

def mothership_repair(session, status):
    if status.get("needs_repair"):
        try:
            r = session.post(f"{BASE_URL}/mothership/repair", data={'repairall': 1})
            log(f"Mothership repair attempted. Response code: {r.status_code}")
        except Exception as e:
            log(f"Mothership repair failed: {e}")
        delay_action()
    else:
        log("No mothership repairs needed.")

def raid(session, target):
    try:
        r = session.post(f"{BASE_URL}/attack/raid", data={'target_id': target['id'], 'attacks': target['attacks']})
        log(f"Raided target {target['id']} ({target['spice']} spice). Response code: {r.status_code}")
        delay_action()
        return r.text
    except Exception as e:
        log(f"Raid on target {target['id']} failed: {e}")
        delay_action()
        return "error"