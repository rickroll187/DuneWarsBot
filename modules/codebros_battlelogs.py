from config import SETTINGS, log

def log_battle_result(battle_type, opponent, outcome, loot=0, details=""):
    report = {
        "type": battle_type,
        "opponent": opponent,
        "outcome": outcome,
        "loot": loot,
        "details": details,
    }
    SETTINGS["BATTLE_HISTORY"].append(report)
    log.info(f"[Battle Report] {battle_type} vs {opponent}: {outcome} | Loot: {loot} | {details}")

def get_latest_reports(n=10):
    return SETTINGS["BATTLE_HISTORY"][-n:]

def log_spy_report(target, outcome, details=""):
    report = {
        "type": "spy",
        "target": target,
        "outcome": outcome,
        "details": details,
    }
    SETTINGS["BATTLE_HISTORY"].append(report)
    log.info(f"[Spy Report] Target: {target} | Outcome: {outcome} | {details}")
