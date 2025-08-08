import time
import random
from selenium.webdriver.common.by import By

def scan_battle_logs(driver):
    """Scan the DuneWars battle logs and return a list of incoming attacks."""
    BATTLE_LOGS_URL = "https://dunewars.net/battle-logs"
    attacks = []
    try:
        driver.get(BATTLE_LOGS_URL)
        time.sleep(random.uniform(1.5, 2.2))
        table = driver.find_element(By.XPATH, "//h3[contains(text(),'Incoming Attacks')]/ancestor::div[contains(@class,'card')]/div[contains(@class,'card-body')]//table")
        rows = table.find_elements(By.XPATH, ".//tbody/tr")
        for row in rows:
            tds = row.find_elements(By.TAG_NAME, "td")
            if len(tds) < 6:
                continue
            time_str = tds[0].text.strip()
            enemy_cell = tds[1]
            try:
                attacker = enemy_cell.find_element(By.TAG_NAME, "a").text.strip()
            except Exception:
                attacker = enemy_cell.text.strip()
            turns = int(tds[2].text.strip().replace(",", ""))
            attack_strength = int(tds[3].text.strip().replace(",", ""))
            status = "onliner" if "online" in attacker.lower() else "offline"
            attacks.append({
                "time": time_str,
                "attacker": attacker,
                "turns": turns,
                "attack_strength": attack_strength,
                "status": status,
            })
        print(f"[Code Bros] Found {len(attacks)} incoming attacks in battle logs!")
    except Exception as e:
        print(f"[Code Bros] Failed to scan battle logs: {e}")
    return attacks