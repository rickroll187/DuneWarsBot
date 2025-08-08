import csv
import os

DATA_PATH = "data/gameplay_data.csv"

def log_gameplay(features, result):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([*features, result])