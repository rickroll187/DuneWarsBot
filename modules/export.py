"""
Google Sheets/Excel Export - Code Bros
Export your stats for the ultimate spreadsheet flex.
"""
import csv
import os
from config import CSV_STATS_PATH, log

def export_to_excel(filename="export_stats.csv"):
    """Copies your stats CSV to a user-friendly Excel/Sheets file."""
    if not os.path.exists(CSV_STATS_PATH):
        log("No stats to export yet, bro!")
        return
    with open(CSV_STATS_PATH, "r") as infile, open(filename, "w", newline='') as outfile:
        for line in infile:
            outfile.write(line)
    log(f"Exported stats to {filename} for maximum spreadsheet glory.")

# For Google Sheets: upload export_stats.csv after running the above function.