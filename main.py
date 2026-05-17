import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Initialize Chrome WebDriver
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 50)

# Navigate to the URL
driver.get("https://www.saucedemo.com/inventory.html")

# Maximize the browser window for better visibility
driver.maximize_window()

# Set an implicit wait time of 30 seconds to handle dynamic elements
driver.implicitly_wait(30)

# Testing for positive login
# On the home page Find the username field by its xpath and enter a positive username
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input").send_keys("performance_glitch_user")
time.sleep(10)

# On the home page Find the password field by its xpath and enter password
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input").send_keys('secret_sauce')
time.sleep(10)

# Find the login button using ID and click on it
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input").click()
time.sleep(10)
# assert driver.title == "Swag Labs"

if "Swag Labs" in driver.title:
    print("TEST PASSED: User logged in successfully")
else:
    print("TEST FAILED: User not on login page")

driver.quit()

