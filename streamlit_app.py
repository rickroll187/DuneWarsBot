import streamlit as st
from config import SETTINGS, log
from modules import (
    bank, combat, train, repair, upgrade, research, spy, anti_covert,
    enemy_stats, battle_reports, custom_actions, resource_management,
    enemy_watchlist, stats_graphs,
    battle_automation, defense_planning, enemy_analysis, adaptive_ai,
    backups, advanced_visualization, historical_analysis
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

# == SIDEBAR CONTROLS ==
st.sidebar.header("Code Bros Bot Controls")
SETTINGS["AUTO_FARM"] = st.sidebar.toggle("Auto Farm", SETTINGS["AUTO_FARM"])
SETTINGS["FARM_AMOUNT"] = st.sidebar.slider("Farm Amount", 1000, 50000, SETTINGS["FARM_AMOUNT"], step=1000)
SETTINGS["AUTO_RAID"] = st.sidebar.toggle("Auto Raid", SETTINGS["AUTO_RAID"])
SETTINGS["RAID_AMOUNT"] = st.sidebar.slider("Raid Amount", 1000, 50000, SETTINGS["RAID_AMOUNT"], step=1000)
SETTINGS["RAID_MAX_TARGETS"] = st.sidebar.slider("Max Raid Targets", 1, 10, SETTINGS["RAID_MAX_TARGETS"])
SETTINGS["AUTO_TRAIN"] = st.sidebar.toggle("Auto Train", SETTINGS["AUTO_TRAIN"])
SETTINGS["TRAIN_AMOUNT"] = st.sidebar.slider("Train Amount", 1, 100, SETTINGS["TRAIN_AMOUNT"])
SETTINGS["AUTO_REPAIR"] = st.sidebar.toggle("Auto Repair", SETTINGS["AUTO_REPAIR"])
SETTINGS["REPAIR_AMOUNT"] = st.sidebar.slider("Repair Amount", 100, 5000, SETTINGS["REPAIR_AMOUNT"], step=100)
SETTINGS["AUTO_UPGRADE"] = st.sidebar.toggle("Auto Upgrade", SETTINGS["AUTO_UPGRADE"])
SETTINGS["UPGRADE_SPICE_THRESHOLD"] = st.sidebar.slider("Upgrade Spice Threshold", 1000, 50000, SETTINGS["UPGRADE_SPICE_THRESHOLD"], step=1000)
SETTINGS["AUTO_RESEARCH"] = st.sidebar.toggle("Auto Research", SETTINGS["AUTO_RESEARCH"])
SETTINGS["AUTO_SPY"] = st.sidebar.toggle("Auto Spy Network", SETTINGS["AUTO_SPY"])
SETTINGS["SPY_COUNT"] = st.sidebar.slider("Number of Spies", 1, 20, SETTINGS["SPY_COUNT"])
SETTINGS["SPY_MISSION"] = st.sidebar.selectbox(
    "Spy Mission", ["scout", "sabotage", "intel"],
    index=["scout", "sabotage", "intel"].index(SETTINGS["SPY_MISSION"])
)
SETTINGS["AUTO_ANTICOVERT"] = st.sidebar.toggle("Auto Anti-Covert Ops", SETTINGS["AUTO_ANTICOVERT"])
SETTINGS["ANTICOVERT_SCAN_COUNT"] = st.sidebar.slider("Anti-Covert Scan Count", 1, 10, SETTINGS["ANTICOVERT_SCAN_COUNT"])
SETTINGS["ANTICOVERT_STRATEGY"] = st.sidebar.selectbox(
    "Anti-Covert Strategy", ["scan", "trap", "counter-intel"],
    index=["scan", "trap", "counter-intel"].index(SETTINGS["ANTICOVERT_STRATEGY"])
)
SETTINGS["SHOW_ENEMY_STATS"] = st.sidebar.toggle("Show Enemy Stats", SETTINGS["SHOW_ENEMY_STATS"])

macro_actions = st.sidebar.text_input("Custom Macro (comma separated)", value="raid,spy,upgrade")
macro_list = [a.strip() for a in macro_actions.split(",") if a.strip()]
if st.sidebar.button("Run Macro"):
    custom_actions.run_macro(macro_list)

if st.sidebar.button("Backup Settings"):
    backups.backup_settings()
if st.sidebar.button("Restore Settings"):
    backups.restore_settings()

# == MAIN LOOP ==
def bot_loop():
    while st.session_state["run_bot"]:
        bank.run(None, SETTINGS["FARM_AMOUNT"])
        combat.run(None, SETTINGS["RAID_AMOUNT"], SETTINGS["RAID_MAX_TARGETS"])
        train.run(None, SETTINGS["TRAIN_AMOUNT"])
        repair.run(None, SETTINGS["REPAIR_AMOUNT"])
        upgrade.run(None, SETTINGS["UPGRADE_SPICE_THRESHOLD"])
        research.run(None)
        spy.run(None, SETTINGS["SPY_COUNT"], SETTINGS["SPY_MISSION"])
        anti_covert.run(None, SETTINGS["ANTICOVERT_SCAN_COUNT"], SETTINGS["ANTICOVERT_STRATEGY"])
        enemy_stats.log_enemy_stats()
        # Battle Automation
        result = battle_automation.auto_battle(SETTINGS["ENEMY_LIST"][0])
        battle_reports.log_battle_result("battle", result["enemy"], result["outcome"], loot=result["loot"])
        # Defense Planning
        defense_planning.plan_defense()
        # Advanced Enemy Analysis
        analysis = enemy_analysis.analyze_enemies()
        # Adaptive AI
        adaptive_ai.adapt_strategy()
        # Resource Management
        resource_management.auto_bank_or_spend(25000)
        # Enemy Watchlist Alerts
        enemy_watchlist.alert_if_enemy_changes(enemy_stats.get_enemy_stats())
        # Stats Graphs
        stats_graphs.record_stats("Spice", SETTINGS["FARM_AMOUNT"])
        # Advanced Visualization
        # (called in UI below)
        # Historical Analysis
        # (called in UI below)
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

if SETTINGS.get("ENABLE_BATTLE_REPORTS", True):
    st.subheader("Battle Reports (Last 10)")
    for report in battle_reports.get_latest_reports(10):
        st.write(
            f"[{report['type'].title()}] vs {report.get('opponent', report.get('target', ''))}: {report['outcome']} | Loot: {report.get('loot', '')} | {report.get('details', '')}"
        )

if SETTINGS.get("SHOW_ENEMY_STATS", True):
    st.subheader("Enemy Stats (Live)")
    for enemy in enemy_stats.get_enemy_stats():
        st.write(
            f"**{enemy['name']}** | Army: {enemy['army']} | Defense: {enemy['defense']} | Spice: {enemy['spice']} | Spies: {enemy['spies']}"
        )

stats_graphs.show_stats_graph()
advanced_visualization.show_multi_stat_dashboard()
historical_analysis.show_historical_stats()

st.caption("Code Bros: The dashboard so cool, even enemy spies want to watch.")

st.info("Why do Code Bros add every function? Because domination is a team sport, and our team is undefeated! 😎")
