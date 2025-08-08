"""
Historical Data & Opponent Tracking - Code Bros
Tracks stats for graphing, CSV, and smarter decisions!
"""
import csv
import datetime
from config import CSV_STATS_PATH, log

def log_performance(stats):
    """Append a stats dict to CSV for performance graphing."""
    row = [datetime.datetime.utcnow().isoformat()] + [stats[k] for k in sorted(stats)]
    with open(CSV_STATS_PATH, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
    log(f"Performance logged: {row}")

def track_opponent(target_id, army, defense, last_seen):
    """Track rivals for smart raiding/defense."""
    # For demo: Append to a simple CSV. Expand to DB for pro use.
    with open("opponent_tracker.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([target_id, army, defense, last_seen])
    log(f"Tracked opponent {target_id}: army={army}, defense={defense}, last_seen={last_seen}")