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

# Switch to the CAPTCHA iframe
iframe = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
driver.switch_to.frame(iframe)

# Find the checkbox and click it
checkbox = driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border")

# Human-like random delay
time.sleep(random.uniform(1.0, 2.5))

# Move mouse near the checkbox using PyAutoGUI (optional, for human-like behavior)
# import pyautogui
# pyautogui.moveTo(checkbox.location['x'] + 5, checkbox.location['y'] + 5, duration=random.uniform(0.5, 1.0))

# Click the checkbox
checkbox.click()

print("Checkbox clicked! Now handle CAPTCHA manually if needed.")

# Wait before closing
time.sleep(10)
driver.quit()

// --- Tiny web server for Render ---
const http = require("http");
http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("Bot is running\n");
}).listen(process.env.PORT || 3000);
