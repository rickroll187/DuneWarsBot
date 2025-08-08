import streamlit as st
import time
import yaml

# Load config
with open("codebros_config.yaml") as f:
    CONFIG = yaml.safe_load(f)

# Example: Replace these with your real getter functions or shared state
def get_spice():
    # TODO: wire to your bot's live value (file, API, or memory)
    return "1,234,567"

def get_bank():
    return "9,876,543"

def get_mode():
    return CONFIG.get("mode", "???")

def get_attacks():
    # TODO: wire to your bot's live value
    # Example attack list
    return [
        {"attacker": "BaronHarkonnen", "turns": 2, "attack_strength": 5000000, "status": "onliner"},
        {"attacker": "PaulMuadDib", "turns": 1, "attack_strength": 3500000, "status": "offline"},
    ]

def code_bros_joke():
    jokes = [
        "This dashboard is spicier than a sandworm chili.",
        "If bots had a party, Streamlit would DJ.",
        "Waiting for an attack? Just chill and bank.",
        "Code Bros: always one step ahead—and cracking jokes.",
        "Mentats wish they had dashboards this cool.",
    ]
    return jokes[int(time.time()) % len(jokes)]

st.set_page_config(page_title="Code Bros DuneWars Dashboard", page_icon="🏄‍♂️", layout="wide")
st.title("🚀 Code Bros DuneWars Web Dashboard 🚀")
st.caption("Easy, live, and full of spice.")

col1, col2, col3 = st.columns(3)
col1.metric("Spice (on hand)", get_spice())
col2.metric("Banked Spice", get_bank())
col3.metric("Mode", get_mode())

st.divider()

st.header("Incoming Attacks")
attacks = get_attacks()
if attacks:
    for atk in attacks:
        st.write(f"**{atk['attacker']}** | Turns: {atk['turns']} | Strength: {atk['attack_strength']:,} | Status: {atk['status']}")
else:
    st.write("No incoming attacks. All quiet on Arrakis.")

st.divider()
st.info(code_bros_joke())

# Optional: auto-refresh every 10 seconds
st.experimental_rerun_interval = 10  # Streamlit v1.32+ only; otherwise use a hack below
if st.button("Refresh Dashboard"):
    st.experimental_rerun()

# Hack for older Streamlit: ask users to hit the refresh button

st.caption("Made by Code Bros. If you see an onliner—bank, joke, and party!")