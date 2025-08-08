import random
import time

def stealth_wait(duration=None):
    """
    Wait with human-like randomness, mouse moves, scrolls, and AFK breaks.
    If STEALTH is enabled in config, uses more advanced random pauses and 'distraction' moments.
    """
    if not STEALTH:
        time.sleep(duration or random.uniform(1, 2))
        return
    # Simulate 'thinking', fidgeting, or a Code Bro break
    total_sleep = duration or random.uniform(1.5, 3)
    slice_count = random.randint(2, 5)
    for _ in range(slice_count):
        # Simulate micro-movements or distraction
        micro_sleep = total_sleep / slice_count * random.uniform(0.6, 1.4)
        time.sleep(micro_sleep)
        # Placeholder for real mouse movement or scrolling:
        if random.random() < 0.3:
            code_bros_log("Stealth mode: Code Bro is 'checking a message' or moving the mouse.")
    # Chance for a longer AFK break
    if random.random() < 0.05:
        afk_time = random.uniform(7, 18)
        code_bros_log(f"Stealth mode: Code Bro is AFK for {afk_time:.1f} seconds (bathroom break 🏄‍♂️).")
        time.sleep(afk_time)