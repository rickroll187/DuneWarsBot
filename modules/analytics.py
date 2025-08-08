import csv
import os
import time
from datetime import datetime

STATS_FILE = "data/bot_stats.csv"
STREAKS_FILE = "data/bot_streaks.json"

def ensure_stats_file():
    if not os.path.exists(STATS_FILE):
        with open(STATS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp", "spice", "banked_spice", "raids", "wins", "losses",
                "mothership_hp", "mothership_max_hp"
            ])

def log_stats(spice, banked_spice, raids, wins, losses, mothership_hp, mothership_max_hp):
    ensure_stats_file()
    with open(STATS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.utcnow().isoformat(),
            spice, banked_spice, raids, wins, losses,
            mothership_hp, mothership_max_hp
        ])

def load_history(limit=200):
    ensure_stats_file()
    with open(STATS_FILE) as f:
        rows = list(csv.DictReader(f))
        if limit:
            rows = rows[-limit:]
    return rows

def get_time_series(metric, limit=200):
    rows = load_history(limit)
    return [float(row[metric]) for row in rows], [row["timestamp"] for row in rows]

def get_latest_streaks():
    import json
    if not os.path.exists(STREAKS_FILE):
        return {"win_streak": 0, "loss_streak": 0, "best_win_streak": 0, "best_loss_streak": 0}
    with open(STREAKS_FILE) as f:
        return json.load(f)

def update_streak(win):
    # win: True for win, False for loss
    import json
    streaks = get_latest_streaks()
    if win:
        streaks["win_streak"] += 1
        streaks["loss_streak"] = 0
        streaks["best_win_streak"] = max(streaks["win_streak"], streaks["best_win_streak"])
    else:
        streaks["loss_streak"] += 1
        streaks["win_streak"] = 0
        streaks["best_loss_streak"] = max(streaks["loss_streak"], streaks["best_loss_streak"])
    with open(STREAKS_FILE, "w") as f:
        json.dump(streaks, f)