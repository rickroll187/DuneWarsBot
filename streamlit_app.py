import threading
from selenium import webdriver

# Import your modules
from modules.combat import run as raid_run
from modules.bank import run as bank_run
from modules.repair import run as repair_run
from modules.train import run as train_run
from modules.upgrade import run as upgrade_run
from modules.research import run as research_run
from modules.mothership import run as mothership_run

st.set_page_config(page_title="Code Bros DuneWarsBot Dashboard", layout="wide")

st.title("🦾 Code Bros DuneWarsBot: Ultimate Control Panel")

# --- Selenium Driver Setup (BRO WARNING: configure as needed) ---
@st.cache_resource(show_spinner=False)
def get_driver():
    try:
        driver = webdriver.Firefox()  # Change to webdriver.Chrome() if you use Chrome
        return driver
    except Exception as e:
        st.error(f"Failed to launch Selenium driver: {e}")
        return None

driver = get_driver()

# --- Bro logging (thread-safe) ---
log_container = st.container()
log_cache = []

def bro_log(msg):
    log_cache.append(msg)
    with log_container:
        st.write(msg)

# --- Threaded runner ---
def threaded_run(func, *args):
    def wrapper():
        bro_log(f"Running {func.__name__}...")
        try:
            func(*args)
            bro_log(f"{func.__name__} completed!")
        except Exception as e:
            bro_log(f"Error in {func.__name__}: {e}")
    threading.Thread(target=wrapper).start()

# --- UI Controls ---
st.subheader("Choose your action, bro:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔥 Attack/Raid"):
        threaded_run(raid_run, driver)
    if st.button("🏦 Bank Spice"):
        threaded_run(bank_run, driver)
    if st.button("🛠️ Repair Troops"):
        threaded_run(repair_run, driver)

with col2:
    if st.button("💪 Train Troops"):
        threaded_run(train_run, driver)
    if st.button("⬆️ Upgrade Stuff"):
        threaded_run(upgrade_run, driver)
    if st.button("🧪 Research"):
        threaded_run(research_run, driver)

with col3:
    if st.button("🚀 Mothership Upkeep"):
        threaded_run(mothership_run, driver)

st.divider()
st.subheader("📜 Bot Logs")
for line in log_cache[-30:]:
    st.write(line)

st.info("Code Bros tip: Smash those buttons, level up, and let the spice flow! 😎")

# Bro Code: Add more features as you wish!
