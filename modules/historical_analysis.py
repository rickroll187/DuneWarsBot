from config import SETTINGS
import streamlit as st
import pandas as pd

def show_historical_stats():
    if SETTINGS["STATS_HISTORY"]:
        st.subheader("Historical Performance")
        df = pd.DataFrame(SETTINGS["STATS_HISTORY"])
        st.line_chart(df["value"])
        # Date-range selector (if you add timestamps)
        # st.date_input("Select range", ...)
