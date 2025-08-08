"""
Dynamic Strategy Adaptation - Code Bros
Adapts raid, defense, and economy based on real-time empire status!
"""
import random
from config import log

# Example: Smart raid target deprioritization and farming
raid_history = {}

def record_raid_result(target_id, success):
    """Track raid results for dynamic targeting."""
    if target_id not in raid_history:
        raid_history[target_id] = {"success": 0, "fail": 0}
    if success:
        raid_history[target_id]["success"] += 1
    else:
        raid_history[target_id]["fail"] += 1

def get_raid_priority(target):
    """Lower priority for failed targets, higher for successful ones."""
    tid = target["id"]
    stats = raid_history.get(tid, {"success": 1, "fail": 0})  # Start optimistic
    return stats["success"] / max(1, stats["fail"] + 1) * target["spice"]

def sort_targets_dynamic(targets):
    """Sorts targets using dynamic priorities for easier farming."""
    return sorted(targets, key=get_raid_priority, reverse=True)

def should_shift_economy(spice, upgrades_pending, research_pending):
    """Switch spending mode if spice is stacking up or key upgrades are waiting."""
    if spice > 50000 or upgrades_pending or research_pending:
        log("Economy shift: prioritizing upgrades/research due to high spice or pending tasks.")
        return True
    return False

def monitor_defense(attacks_received):
    """If under attack, increase defense spending/training/repairs."""
    if attacks_received > 2:
        log("Defense alert: Multiple attacks detected! Boosting defense mode.")
        return "DEFENSE"
    return "NORMAL"