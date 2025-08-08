import streamlit as st

from modules import (
    bank,
    combat,
    train,
    repair,
    upgrade,
    research,
    spy,
    anti_covert,
    enemy_stats,
    codebros_battlelogs,   # <-- updated import name!
    custom_actions,
    enemy_watchlist,
    stats_graphs
)

st.set_page_config(page_title="DuneWarsBot", layout="wide")
st.title("💣 DuneWarsBot — Code Bros Edition")

st.write("Welcome to DuneWarsBot! The Code Bros bring you the spiciest bot in the desert. More features coming soon!")

# Example placeholder sections for each module
st.header("Bank")
st.info(bank.get_bank_status() if hasattr(bank, "get_bank_status") else "Bank module loaded. Functionality coming soon!")

st.header("Combat")
st.info(combat.get_combat_report() if hasattr(combat, "get_combat_report") else "Combat module loaded. Functionality coming soon!")

st.header("Train")
st.info(train.train_units() if hasattr(train, "train_units") else "Train module loaded. Functionality coming soon!")

st.header("Repair")
st.info(repair.repair_units() if hasattr(repair, "repair_units") else "Repair module loaded. Functionality coming soon!")

st.header("Upgrade")
st.info(upgrade.upgrade_units() if hasattr(upgrade, "upgrade_units") else "Upgrade module loaded. Functionality coming soon!")

st.header("Research")
st.info(research.research_units() if hasattr(research, "research_units") else "Research module loaded. Functionality coming soon!")

st.header("Spy Network")
st.info(spy.spy_report() if hasattr(spy, "spy_report") else "Spy module loaded. Functionality coming soon!")

st.header("Anti-Covert Ops")
st.info(anti_covert.scan_for_intruders() if hasattr(anti_covert, "scan_for_intruders") else "Anti-Covert module loaded. Functionality coming soon!")

st.header("Enemy Stats")
st.info(enemy_stats.get_stats() if hasattr(enemy_stats, "get_stats") else "Enemy stats module loaded. Functionality coming soon!")

st.header("Battle Logs")
st.info(codebros_battlelogs.get_battle_log() if hasattr(codebros_battlelogs, "get_battle_log") else "Battle logs module loaded. Functionality coming soon!")

st.header("Custom Actions")
st.info(custom_actions.get_actions() if hasattr(custom_actions, "get_actions") else "Custom actions module loaded. Functionality coming soon!")

st.header("Resource Management")
st.info(resource_management.get_resources() if hasattr(resource_management, "get_resources") else "Resource management module loaded. Functionality coming soon!")

st.header("Enemy Watchlist")
st.info(enemy_watchlist.get_watchlist() if hasattr(enemy_watchlist, "get_watchlist") else "Enemy watchlist module loaded. Functionality coming soon!")

st.header("Stats Graphs")
st.info(stats_graphs.show_graphs() if hasattr(stats_graphs, "show_graphs") else "Stats graphs module loaded. Functionality coming soon!")

st.markdown("---")
st.caption("🦾 Code Bros: We code the spice, we crack the jokes. If you hit an error, drop it here and we'll roast it!")

# Joke of the day:
st.sidebar.title("Code Bros Joke")
st.sidebar.markdown("> Why do Code Bros love Streamlit?\n> Because launching a bot should be as easy as flexing your biceps, bro! 😎")
