import streamlit as st
import random

def get_empire_map_data():
    # Simulate map data (replace with real scraping/game data)
    # Each "cell" is a player: type = 'self', 'enemy', 'spy_target', 'raided', etc.
    grid = []
    for y in range(10):
        row = []
        for x in range(10):
            cell_type = random.choices(
                ["empty", "self", "enemy", "spy_target", "raided"],
                [0.75, 0.04, 0.05, 0.08, 0.08]
            )[0]
            cell = {"type": cell_type, "x": x, "y": y}
            row.append(cell)
        grid.append(row)
    return grid

def render_empire_map():
    st.subheader("🗺️ Empire Map & Known Targets")
    data = get_empire_map_data()
    legend = {
        "empty": "⬜", "self": "🟦", "enemy": "🟥",
        "spy_target": "🟨", "raided": "🟩"
    }
    st.markdown(
        "**Legend:** 🟦=You  🟥=Enemy  🟨=Spy Target  🟩=Recently Raided  ⬜=Empty"
    )
    map_rows = []
    for row in data:
        map_row = ""
        for cell in row:
            map_row += legend[cell["type"]]
        map_rows.append(map_row)
    st.text("\n".join(map_rows))