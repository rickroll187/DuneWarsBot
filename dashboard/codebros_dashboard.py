import streamlit as st
import json
import os

SPY_SAVE_FILE = "spy_targets.json"

def load_spy_targets():
    if not os.path.exists(SPY_SAVE_FILE):
        return []
    with open(SPY_SAVE_FILE, "r") as f:
        return json.load(f)

def emoji_relation(rel):
    return {
        "enemy": "🔥",
        "ally": "🫱🏻‍🫲🏽",
        "recent_attacker": "⚔️",
        "neutral": "🌵",
        "unknown": "❓"
    }.get(rel, "❓")

st.set_page_config(page_title="Code Bros DuneWars Dashboard", page_icon="🏄‍♂️", layout="wide")
st.title("🚀 Code Bros DuneWars Web Dashboard 🚀")
st.caption("Now with a full SPY NETWORK! (Top 200)")

tab1, tab2 = st.tabs(["Live Stats", "Spy Network"])

with tab1:
    st.write("Add your live stats here, bro!")

with tab2:
    st.header("🕵️‍♂️ Spy Network — Top 200 Player Scan")

    # Filter toggles
    filter_relation = st.selectbox(
        "Show Relation",
        ["all", "enemy", "ally", "recent_attacker", "neutral"],
        index=0
    )
    sort_by = st.selectbox(
        "Sort by",
        ["Spice", "Defense", "Last Active", "Name"],
        index=0
    )
    if st.button("Manual Spy Crawl"):
        from spy_network import manual_spy_crawl
        manual_spy_crawl()
        st.success("Spy crawl triggered! Refresh in 10 seconds, bro.")

    spy_targets = load_spy_targets()
    if not spy_targets:
        st.warning("No spy data yet. Wait for crawl or hit 'Manual Spy Crawl'.")
    else:
        # Filter
        if filter_relation != "all":
            spy_targets = [p for p in spy_targets if p.get("relation") == filter_relation]
        # Sort
        if sort_by == "Spice":
            spy_targets = sorted(spy_targets, key=lambda x: -x["spice"])
        elif sort_by == "Defense":
            spy_targets = sorted(spy_targets, key=lambda x: -x["defense"])
        elif sort_by == "Last Active":
            spy_targets = sorted(spy_targets, key=lambda x: x["last_active"])
        elif sort_by == "Name":
            spy_targets = sorted(spy_targets, key=lambda x: x["name"])

        st.write(f"Showing {len(spy_targets)} players")
        st.dataframe([
            {
                "Rank": i + 1,
                "Name": p["name"],
                "Spice": f"{p['spice']:,}",
                "Defense": f"{p['defense']:,}",
                "Last Active": p["last_active"],
                "Alliance": p["alliance"],
                "Relation": emoji_relation(p["relation"]),
            }
            for i, p in enumerate(spy_targets)
        ], use_container_width=True)