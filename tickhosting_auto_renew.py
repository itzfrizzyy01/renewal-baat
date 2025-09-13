from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import threading
import os

# --- Flask Web Server (keep alive on Render) ---
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running\n"

def run_server():
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)

# --- Selenium Bot ---
def run_bot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.binary_location = "/usr/bin/chromium-browser"  # Adjust if needed

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    try:
        driver.get("https://asia.tickhosting.com/server/cca52f8a")
        time.sleep(5)

        # Try to find CAPTCHA iframe and click checkbox
        iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
        driver.switch_to.frame(iframe)
        checkbox = driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border")
        time.sleep(random.uniform(1.0, 3.0))
        checkbox.click()
        print("✅ CAPTCHA checkbox clicked!")
        driver.switch_to.default_content()

        time.sleep(random.uniform(3.0, 6.0))

        # Find and click Renew button
        renew_button = driver.find_element(By.XPATH, "//button[contains(text(),'Renew')]")
        time.sleep(random.uniform(1.0, 2.0))
        renew_button.click()
        print("✅ Renew button clicked!")

    except Exception as e:
        print("❌ Error during automation:", e)

    finally:
        time.sleep(5)
        driver.quit()
        print("✅ Browser closed")

# --- Main ---
if __name__ == "__main__":
    # Start Flask server in a separate thread
    threading.Thread(target=run_server).start()

    # Run the Selenium bot once (or loop as needed)
    run_bot()


