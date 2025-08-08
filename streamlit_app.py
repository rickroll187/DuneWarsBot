import streamlit as st
from config import SETTINGS, log
from modules import (
    bank, combat, train, repair, upgrade, research, spy, anti_covert,
    enemy_stats, battle_reports, custom_actions, resource_management,
    enemy_watchlist, stats_graphs
)
import threading
import time
import logging

DASH_LOG = []

class StreamlitLogHandler(logging.Handler):
    def emit(self, record):
        msg = self.format(record)
        DASH_LOG.append(msg)
        if len(DASH_LOG) > SETTINGS["MAX_LOG_LINES"]:
            DASH_LOG.pop(0)

log.handlers = []
log.addHandler(StreamlitLogHandler())

st.title("Code Bros DuneWarsBot Monster Edition 💪😎")

st.sidebar.header("Code Bros Bot Controls")

# == Feature Toggles ==
SETTINGS["AUTO_FARM"] = st.sidebar.toggle("Auto Farm", SETTINGS["AUTO_FARM"])
SETTINGS["AUTO_RAID"] = st.sidebar.toggle("Auto Raid", SETTINGS["AUTO_RAID"])
SETTINGS["AUTO_TRAIN"] = st.sidebar.toggle("Auto Train", SETTINGS["AUTO_TRAIN"])
SETTINGS["AUTO_REPAIR"] = st.sidebar.toggle("Auto Repair Mothership", SETTINGS["AUTO_REPAIR"])
SETTINGS["AUTO_UPGRADE"] = st.sidebar.toggle("Auto Upgrade", SETTINGS["AUTO_UPGRADE"])
SETTINGS["AUTO_RESEARCH"] = st.sidebar.toggle("Auto Research", SETTINGS["AUTO_RESEARCH"])
SETTINGS["AUTO_SPY"] = st.sidebar.toggle("Auto Spy Network", SETTINGS["AUTO_SPY"])
SETTINGS["AUTO_ANTICOVERT"] = st.sidebar.toggle("Auto Anti-Covert Ops", SETTINGS["AUTO_ANTICOVERT"])

SETTINGS["REPAIR_AMOUNT"] = st.sidebar.slider("Repair Amount", 100, 5000, SETTINGS["REPAIR_AMOUNT"], step=100)

# == ALL IN Mode ==
if st.sidebar.button("Go ALL IN Code Bros Mode"):
    for key in SETTINGS:
        if key.startswith("AUTO_"):
            SETTINGS[key] = True
    st.success("ALL IN mode activated! Every feature firing. 💪")

macro_actions = st.sidebar.text_input("Custom Macro (comma separated)", value="raid,spy,upgrade")
macro_list = [a.strip() for a in macro_actions.split(",") if a.strip()]
if st.sidebar.button("Run Macro"):
    custom_actions.run_macro(macro_list)

def bot_loop():
    while st.session_state["run_bot"]:
        bank.run(None, SETTINGS.get("FARM_AMOUNT", 10000))
        combat.run(None, SETTINGS.get("RAID_AMOUNT", 5000), SETTINGS.get("RAID_MAX_TARGETS", 3))
        train.run(None, SETTINGS.get("TRAIN_AMOUNT", 20))
        repair.run(None, SETTINGS.get("REPAIR_AMOUNT", 500))
        upgrade.run(None, SETTINGS.get("UPGRADE_SPICE_THRESHOLD", 10000))
        research.run(None)
        spy.run(None, SETTINGS.get("SPY_COUNT", 5), SETTINGS.get("SPY_MISSION", "intel"))
        anti_covert.run(None, SETTINGS.get("ANTICOVERT_SCAN_COUNT", 3), SETTINGS.get("ANTICOVERT_STRATEGY", "scan"))
        enemy_stats.log_enemy_stats()
        time.sleep(2)

if "run_bot" not in st.session_state:
    st.session_state["run_bot"] = False
    st.session_state["bot_thread"] = None

if st.button("Start Code Bros Bot", disabled=st.session_state["run_bot"]):
    st.session_state["run_bot"] = True
    st.session_state["bot_thread"] = threading.Thread(target=bot_loop, daemon=True)
    st.session_state["bot_thread"].start()
    st.success("Bot started! Watch it work below.")

if st.button("Stop Bot", disabled=not st.session_state["run_bot"]):
    st.session_state["run_bot"] = False
    st.success("Bot stopped!")

st.subheader("Bot Activity Log (Real Time)")
for msg in DASH_LOG[-40:]:
    st.write(msg)

st.caption("Code Bros: Domination, one toggle at a time. Turn it off if you want scars, bro! 😎")
