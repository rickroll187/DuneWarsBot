from config import SETTINGS
import streamlit as st

def show_multi_stat_dashboard():
    if SETTINGS["ENABLE_STATS_GRAPHS"] and SETTINGS["STATS_HISTORY"]:
        st.subheader("Advanced Domination Dashboard")
        # Example: show bar chart for last 10 stats
        st.bar_chart([s["value"] for s in SETTINGS["STATS_HISTORY"][-10:]])
        # Example: pie chart for army distribution
        st.subheader("Army Distribution")
        army_dict = {e["name"]: e["army"] for e in SETTINGS["ENEMY_LIST"]}
        st.write(army_dict)
        st.pyplot(st.get_option("deprecation.showPyplotGlobalUse"))
