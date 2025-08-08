"""
Smart Scheduler for DuneWars - Code Bros
Keeps your empire running when the competition is napping.
"""
from config import SMART_SCHEDULER, FARM_PEAK_HOURS, log
import datetime

def should_run_now():
    if not SMART_SCHEDULER:
        return True
    now = datetime.datetime.utcnow()
    start, end = FARM_PEAK_HOURS
    if start < end:
        should_run = start <= now.hour < end
    else:
        should_run = now.hour >= start or now.hour < end
    if not should_run:
        log(f"Scheduler: Not in peak hours ({start}:00-{end}:00 UTC). Waiting for the perfect time.")
    return should_run