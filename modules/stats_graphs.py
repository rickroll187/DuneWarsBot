from config import SETTINGS
import streamlit as st

def record_stats(stat_name, value):
    SETTINGS["STATS_HISTORY"].append({"stat": stat_name, "value": value})

def show_stats_graph():
    if SETTINGS["ENABLE_STATS_GRAPHS"]:
        if SETTINGS["STATS_HISTORY"]:
            st.subheader("Domination Over Time (Code Bros Style)")
            stat_names = [s["stat"] for s in SETTINGS["STATS_HISTORY"]]
            values = [s["value"] for s in SETTINGS["STATS_HISTORY"]]
            st.line_chart(values)
