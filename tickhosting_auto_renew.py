from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Setup Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the renewal page
driver.get("https://asia.tickhosting.com/server/cca52f8a")

# Wait for page to load
time.sleep(5)

try:
    # Switch to CAPTCHA iframe
    iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
    driver.switch_to.frame(iframe)

    # Find the checkbox
    checkbox = driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border")

    # Human-like random delay
    time.sleep(random.uniform(1.0, 2.5))

    # Click the checkbox
    checkbox.click()

    print("CAPTCHA checkbox clicked!")

    # Switch back to main content
    driver.switch_to.default_content()

    # Wait for user or CAPTCHA challenge to settle
    time.sleep(random.uniform(3.0, 5.0))

    # Find the Renew button (adjust if needed)
    renew_button = driver.find_element(By.XPATH, "//button[contains(text(),'Renew')]")

    # Move with random delay
    time.sleep(random.uniform(1.0, 2.0))

    # Click the Renew button
    renew_button.click()

    print("Renew button clicked!")

except Exception as e:
    print("Error:", e)

# Wait before closing to observe the result
time.sleep(5)
driver.quit()


// --- Tiny web server for Render ---
const http = require("http");
http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("Bot is running\n");
}).listen(process.env.PORT || 3000);
