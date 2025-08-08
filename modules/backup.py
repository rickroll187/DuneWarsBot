"""
Auto-Backup & Recovery - Code Bros
Keeps your bot's config & stats safe from sandworms (and crashes).
"""
import shutil
import os
import datetime
from config import LOG_FILE_PATH, CSV_STATS_PATH, log

BACKUP_DIR = "backups"

def backup_file(src):
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    dst = os.path.join(BACKUP_DIR, f"{os.path.basename(src)}.{timestamp}.bak")
    shutil.copy2(src, dst)
    log(f"Backed up {src} to {dst}")

def backup_all():
    for f in [LOG_FILE_PATH, CSV_STATS_PATH]:
        if os.path.exists(f):
            backup_file(f)

def restore_latest(filename):
    backups = [b for b in os.listdir(BACKUP_DIR) if b.startswith(os.path.basename(filename))]
    if not backups:
        log(f"No backups found for {filename}")
        return
    latest = sorted(backups)[-1]
    shutil.copy2(os.path.join(BACKUP_DIR, latest), filename)
    log(f"Restored {filename} from {latest}")