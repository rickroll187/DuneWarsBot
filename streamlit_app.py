import streamlit as st

# Import your modules
from modules import (
    bank,
    combat,
    train,
    repair,
    upgrade,
    research,
    # spy,         # Uncomment when spy.py is ready!
    anti_covert
)

st.set_page_config(page_title="DuneWarsBot", layout="wide")
st.title("💣 DuneWarsBot — Code Bros Edition")

# Example: Use functions from your modules
st.header("Bank Status")
if hasattr(bank, "get_bank_status"):
    st.write(bank.get_bank_status())
else:
    st.info("Bank module loaded, but no get_bank_status() found.")

st.header("Combat Zone")
if hasattr(combat, "get_combat_report"):
    st.write(combat.get_combat_report())
else:
    st.info("Combat module loaded, but no get_combat_report() found.")

st.header("Training Grounds")
if hasattr(train, "train_units"):
    st.write(train.train_units())
else:
    st.info("Train module loaded, but no train_units() found.")

# Continue adding sections for other modules...

# Uncomment this when spy.py is working!
# st.header("Spy Network")
# if hasattr(spy, "get_spy_log"):
#     st.write(spy.get_spy_log())
# else:
#     st.info("Spy module loaded, but no get_spy_log() found.")

st.header("Anti-Covert Ops")
if hasattr(anti_covert, "scan_for_intruders"):
    st.write(anti_covert.scan_for_intruders())
else:
    st.info("Anti-Covert module loaded, but no scan_for_intruders() found.")

st.markdown("---")
st.caption("🦾 Code Bros: We code the spice, we crack the jokes. If you hit an error, drop it here and we'll roast it!")

# 🦾 Joke of the day:
st.sidebar.title("Code Bros Joke")
st.sidebar.markdown("> Why do Code Bros love Streamlit?\n> Because launching a bot should be as easy as flexing your biceps, bro! 😎")
