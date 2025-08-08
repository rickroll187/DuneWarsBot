import time
import config
from selenium.webdriver.common.by import By

# === CONFIGURE YOUR FARMING THRESHOLD BELOW ===
MIN_SPICE = 10_000_000_000  # Only hit targets with at least this much spice

def run(driver):
    print("[Code Bros] The spice must flow... but only to those worth it! 🚜🌶️")

    driver.get(config.DASHBOARD_URL)
    time.sleep(2)

    # Find the table
    table = driver.find_element(By.CSS_SELECTOR, "table.table-vcenter")
    rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # Skip header row

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) < 7:
            continue  # skip if not enough columns

        # Get available spice ("Hidden" means can't farm)
        spice_text = cells[5].text.strip().replace(",", "")
        try:
            spice = int(spice_text)
        except ValueError:
            print("[Code Bros] Target has hidden spice, skipping.")
            continue

        # Get rank and username
        rank = cells[0].text.strip()
        name_link = cells[1].find_element(By.TAG_NAME, "a")
        name = name_link.text.strip()
        print(f"[Code Bros] {rank} | {name} | Spice: {spice:,}")

        if spice < MIN_SPICE:
            print(f"[Code Bros] Not enough spice. Skipping {name}.")
            continue

        # Find the "Raid" form (change to "spy" or "attack" if you want)
        actions_cell = cells[6]
        raid_form = None
        for form in actions_cell.find_elements(By.TAG_NAME, "form"):
            if "/attack/raid" in form.get_attribute("action"):
                raid_form = form
                break

        if raid_form:
            raid_form.submit()
            print(f"[Code Bros] RAIDING {name} for that sweet, sweet spice! 💰")
            time.sleep(1)  # Don't be too fast, spice bro
        else:
            print(f"[Code Bros] No raid form found for {name}, skipping...")

    print("[Code Bros] Done farming, bro. The sandworms are jealous!")