import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Code Bros DuneWars Bot CLI")
    parser.add_argument("--train-only", action="store_true", help="Only run training module")
    parser.add_argument("--raid", action="store_true", help="Only run raiding module")
    parser.add_argument("--stats", action="store_true", help="Print stats and exit")
    parser.add_argument("--run-all", action="store_true", help="Run all modules (default behavior)")
    parser.add_argument("--dashboard", action="store_true", help="Start the web dashboard")
    return parser.parse_args()