import yaml

CONFIG_FILE = "codebros_config.yaml"

def read_config():
    with open(CONFIG_FILE) as f:
        return yaml.safe_load(f)

def write_config(cfg):
    with open(CONFIG_FILE, "w") as f:
        yaml.safe_dump(cfg, f)

def update_config(updates):
    cfg = read_config()
    cfg.update(updates)
    write_config(cfg)

def reload_config():
    # Optionally: signal running modules to re-read config!
    pass

def get_spice_history():
    # Load from log or CSV
    # Example dummy data for chart
    return [1000000, 1200000, 1500000, 1100000, 1600000]

def get_raid_stats():
    # Example dummy data for chart
    return [1, 2, 1, 3, 2]