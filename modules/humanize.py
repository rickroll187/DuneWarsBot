"""
Extra Humanization - Code Bros
Simulates idle/browsing behavior for stealthy botting.
"""
import random
import time
from config import log

DUMMY_PAGES = [
    "/empire",
    "/upgrades",
    "/research",
    "/leaderboard",
    "/messages",
    "/base",
]

def browse_random_page(session):
    page = random.choice(DUMMY_PAGES)
    log(f"Browsing page {page} to look casual.")
    # TODO: session.get(BASE_URL + page)
    time.sleep(random.uniform(1, 3))

def do_idle_behavior(session, cycles=2):
    for _ in range(random.randint(1, cycles)):
        browse_random_page(session)
        time.sleep(random.uniform(2, 5))