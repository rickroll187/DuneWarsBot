import json

SPY_SAVE_FILE = "data/spy_targets.json"

def enable_spy():
    print("[Spy Network] Enabled.")

def disable_spy():
    print("[Spy Network] Disabled.")

def manual_spy_crawl():
    print("[Spy Network] Manual crawl triggered.")
    crawl_spy_network(force=True)

def crawl_spy_network(force=False):
    # Your spy logic here
    print("[Spy Network] Crawling top 200 players... (mocked)")
    data = [{"name": f"Player{i}", "spice": 1000000+i*10000, "relation": "enemy" if i%2==0 else "neutral"} for i in range(1, 21)]
    with open(SPY_SAVE_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("[Spy Network] Crawl done.")

def get_last_targets():
    try:
        with open(SPY_SAVE_FILE) as f:
            return json.load(f)
    except:
        return []