import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from modules.ai_strategy import load_data, train_ai, predict_ai
from modules.data_logger import log_gameplay
import numpy as np

st.set_page_config(page_title="Code Bros AI Dashboard: Self-Defense Edition 🤖🛡️", layout="centered")
st.title("Code Bros AI Dashboard: Self-Defense, Farm, Raid, Auto & Resource Management 🤖🌶️")
st.write("Attack, defend, farm, raid, automate, manage resources, and analyze—Code Bros style!")

# --- Logging Section ---
st.header("Log New Game & Retrain")

mode_map = {1: "Attack", 0: "Defend"}
mode = st.selectbox("Mode", [1, 0], format_func=lambda x: mode_map[x])

col1, col2, col3 = st.columns(3)
with col1:
    current_spice = st.number_input("Current Spice", min_value=0, value=50)
with col2:
    enemy_strength = st.number_input("Enemy Strength", min_value=0, value=50)
with col3:
    my_defense = st.number_input("My Defense", min_value=0, value=50)

# --- Strategy Toggles ---
st.subheader("Strategy Toggles & Automation")
farm_mode = st.selectbox("Choose Mode:", ["Farm", "Raid"])
war_mode = st.checkbox("Enable War Mode")
auto_train = st.checkbox("Auto-Train")
auto_buy_weapons = st.checkbox("Auto-Buy Weapons")
auto_repair = st.checkbox("Auto-Repair")
mothership = st.checkbox("Mothership Mode (Big Move)")

# --- Resources and Attack State ---
st.subheader("Resource & Threat State")
current_resources = st.number_input("Current Resources", min_value=0, value=100)
under_attack_count = st.number_input("Times Attacked in a Row", min_value=0, value=0)

features = [
    mode, current_spice, enemy_strength, my_defense,
    int(farm_mode == "Raid"),
    int(war_mode),
    int(auto_train),
    int(auto_buy_weapons),
    int(auto_repair),
    int(mothership),
    current_resources,
    under_attack_count
]

result = st.selectbox("Result", [1, 0], format_func=lambda x: "Win" if x == 1 else "Loss")

if st.button("Log Game & Retrain"):
    log_gameplay(features, result)
    X, y = load_data()
    if len(X) > 5:
        train_ai(X, y)
        st.success("Game logged and AI retrained, bro! Ready for farm, raid, self-defense, and full-scale war!")
    elif len(X) > 0:
        st.info("Game logged, but you'll need more data for spicy predictions, bro!")
    else:
        st.error("No data yet, bro! Play some games first!")

# --- Prediction Section ---
st.header("Test AI Prediction (Attack/Defend/Farm/Raid/Auto/Defense)")

test_mode = st.selectbox("Test Mode", [1, 0], format_func=lambda x: mode_map[x], key="test_mode")
test_col1, test_col2, test_col3 = st.columns(3)
with test_col1:
    test_current_spice = st.number_input("Test: Current Spice", min_value=0, value=60, key="test_spice")
with test_col2:
    test_enemy_strength = st.number_input("Test: Enemy Strength", min_value=0, value=60, key="test_enemy")
with test_col3:
    test_my_defense = st.number_input("Test: My Defense", min_value=0, value=60, key="test_defense")

test_farm_mode = st.selectbox("Test: Farm/Raid", ["Farm", "Raid"], key="test_farm_mode")
test_war_mode = st.checkbox("Test: Enable War Mode", key="test_war_mode")
test_auto_train = st.checkbox("Test: Auto-Train", key="test_auto_train")
test_auto_buy_weapons = st.checkbox("Test: Auto-Buy Weapons", key="test_auto_buy_weapons")
test_auto_repair = st.checkbox("Test: Auto-Repair", key="test_auto_repair")
test_mothership = st.checkbox("Test: Mothership Mode", key="test_mothership")
test_current_resources = st.number_input("Test: Current Resources", min_value=0, value=100, key="test_resources")
test_under_attack_count = st.number_input("Test: Times Attacked in a Row", min_value=0, value=0, key="test_attacked")

test_features = [
    test_mode, test_current_spice, test_enemy_strength, test_my_defense,
    int(test_farm_mode == "Raid"),
    int(test_war_mode),
    int(test_auto_train),
    int(test_auto_buy_weapons),
    int(test_auto_repair),
    int(test_mothership),
    test_current_resources,
    test_under_attack_count
]

if st.button("Run AI Prediction"):
    pred = predict_ai(test_features)
    action = mode_map[test_mode]
    farm_raid = "RAID" if test_farm_mode == "Raid" else "FARM"
    war = "WAR" if test_war_mode else "PEACE"
    st.write(
        f"AI says: **{'Go for ' + action.upper() + '!' if pred else 'Do NOT ' + action.upper() + ' now.'}** "
        f"(mode: {action}, {farm_raid}, {war}, auto_train={test_auto_train}, "
        f"auto_buy_weapons={test_auto_buy_weapons}, auto_repair={test_auto_repair}, mothership={test_mothership}, "
        f"resources={test_current_resources}, under_attack_count={test_under_attack_count})"
    )

# --- Analytics Section ---
st.header("Gameplay Data & Analytics")
X, y = load_data()
if len(X) > 0:
    st.write(f"Total games logged: **{len(X)}**")
    # Show last 10 games with all toggles
    st.write("Recent games (last 10):")
    def label_bool(val, pos, on="✅", off="❌"):
        return on if val else off

    st.dataframe(
        {
            "Mode": [mode_map[int(row[0])] for row in X[-10:]],
            "Current Spice": [row[1] for row in X[-10:]],
            "Enemy Strength": [row[2] for row in X[-10:]],
            "My Defense": [row[3] for row in X[-10:]],
            "Raid": [label_bool(row[4], 4) for row in X[-10:]],
            "War Mode": [label_bool(row[5], 5) for row in X[-10:]],
            "Auto-Train": [label_bool(row[6], 6) for row in X[-10:]],
            "Auto-Buy": [label_bool(row[7], 7) for row in X[-10:]],
            "Auto-Repair": [label_bool(row[8], 8) for row in X[-10:]],
            "Mothership": [label_bool(row[9], 9, "🛸", "—") for row in X[-10:]],
            "Resources": [row[10] for row in X[-10:]],
            "Attacked xN": [row[11] for row in X[-10:]],
            "Result": ["Win" if r == 1 else "Loss" for r in y[-10:]],
        }
    )
    # Analytics: Attack/Defend split and win rates, Raid/Farm, War Mode
    arrX = np.array(X)
    arrY = np.array(y)
    for m, label in mode_map.items():
        idx = arrX[:, 0] == m
        total = np.sum(idx)
        if total > 0:
            win_rate = np.mean(arrY[idx])
            st.metric(f"{label} win rate", f"{100*win_rate:.1f}%", f"over {total} games")
    for raid in [0, 1]:
        idx = arrX[:, 4] == raid
        label = "RAID" if raid else "FARM"
        total = np.sum(idx)
        if total > 0:
            win_rate = np.mean(arrY[idx])
            st.metric(f"{label} win rate", f"{100*win_rate:.1f}%", f"over {total} games")
    for war in [0, 1]:
        idx = arrX[:, 5] == war
        label = "WAR MODE" if war else "PEACE MODE"
        total = np.sum(idx)
        if total > 0:
            win_rate = np.mean(arrY[idx])
            st.metric(f"{label} win rate", f"{100*win_rate:.1f}%", f"over {total} games")
    # Analytics for self-defense: attacked multiple times
    for threat in [0, 1, 2, 3, 4, 5]:
        idx = arrX[:, 11] == threat
        total = np.sum(idx)
        if total > 0:
            win_rate = np.mean(arrY[idx])
            st.metric(f"Win rate when attacked x{threat}", f"{100*win_rate:.1f}%", f"{total} games")
else:
    st.info("No gameplay data yet. Log some games to see analytics!")

st.markdown("---")
st.caption("Now with farming, raiding, war mode, auto-training, resource management, and tactical defense! Code Bros: we never run out of spice or jokes! 🌶️🛡️")