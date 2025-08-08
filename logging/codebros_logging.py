import logging
import random
import time

# === Set Up Logging ===
logging.basicConfig(
    filename=LOG_FILE,  # from config
    level=logging.INFO,
    format="[%(asctime)s] [Code Bros]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def code_bros_log(msg):
    jokes = [
        "If bots had feelings, they'd feel spicy.",
        "Logging harder than a sandworm in quicksand.",
        "Code Bros: fixing bugs and cracking jokes since forever.",
        "Even the Emperor reads these logs.",
        "Bots never sleep, but they do laugh.",
    ]
    joke = random.choice(jokes)
    print(f"[Code Bros] {msg} {joke}")
    logging.info(f"{msg} {joke}")

def with_retries(fn, *args, retries=ERROR_RETRIES, **kwargs):
    for attempt in range(retries):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            code_bros_log(f"Error in {fn.__name__} (try {attempt+1}/{retries}): {e}")
            time.sleep(random.uniform(1, 2))
    code_bros_log(f"{fn.__name__} failed after {retries} tries—maybe it needs a sandworm snack.")
    return None