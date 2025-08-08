"""
Session Recovery - Code Bros
Keeps your bot rolling even after a sandworm-sized disconnect.
"""
import time
from config import log

def is_session_alive(session):
    """
    Checks if the session is still valid.
    Replace this with a real request for your game/app.
    """
    try:
        # Example: session.get("https://game.url/empire")
        # If you get a 200 or valid response, return True
        # Here we just return True for demo purposes
        return True
    except Exception:
        return False

def recover_session(auth_func, *auth_args, **auth_kwargs):
    """
    Attempts to recover a lost session using the provided authentication function.
    """
    log("Session lost! Attempting auto-recovery...")
    for attempt in range(1, 4):
        try:
            session = auth_func(*auth_args, **auth_kwargs)
            if is_session_alive(session):
                log(f"Session recovery successful on attempt {attempt}!")
                return session
        except Exception as e:
            log(f"Recovery attempt {attempt} failed: {e}")
        time.sleep(2 * attempt)  # Exponential backoff
    log("Session recovery failed. Manual action needed, bro.")
    return None