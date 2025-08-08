from selenium.webdriver.common.by import By
import time
import config

def run(driver):
    print("[CodeBros] You're in! Letting the spice flow... 🌶️")
    driver.get(config.DASHBOARD_URL)
    time.sleep(2)
    # Example action: Print dashboard title
    print(f"[CodeBros] Dashboard Title: {driver.title}")

    # Placeholder for more bot actions
    print("[CodeBros] Add your automation code here, bro!")
    time.sleep(config.AFTER_LOGIN_WAIT)