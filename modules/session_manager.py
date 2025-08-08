"""
Handles login, session management, and user-agent rotation for DuneWars.
"""
import random
import requests
from config import USERNAME, PASSWORD, RANDOMIZE_USER_AGENT, USER_AGENTS, log

BASE_URL = "https://dunewars.net"

def get_user_agent():
    if RANDOMIZE_USER_AGENT:
        return random.choice(USER_AGENTS)
    return USER_AGENTS[0]

def login():
    session = requests.Session()
    session.headers.update({"User-Agent": get_user_agent()})
    login_url = f"{BASE_URL}/login"

    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "submit": "Login"
    }

    log("Logging in with style...")
    resp = session.post(login_url, data=payload)
    if "logout" in resp.text.lower() or resp.url.endswith("/base"):
        log("Login successful! Time to spice up Arrakis.")
        return session
    else:
        log("Login failed. Did you forget your password or your sense of humor?")
        raise Exception("Login failed")