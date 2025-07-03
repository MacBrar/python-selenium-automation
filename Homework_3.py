from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# 1. locators for Create Account on amazon.com
#driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']") amazon logo
#driver.find_element(By.XPATH, "//h1[contains(text(),'Create')]") create account text
#driver.find_element(By.XPATH, "//input[@id='ap_customer_name']") your name field
#driver.find_element(By.XPATH, "//input[@id='ap_customer_name']") your name field
#driver.find_element(By.CSS_SELECTOR, "ap_email") email field
#driver.find_element(By.CSS_SELECTOR, "ap_password") password field
#driver.find_element(By.CSS_SELECTOR, "ap_password_check") re-enter password field
#driver.find_element(By.CSS_SELECTOR, "continue") Create your amazon account button
#driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]" conditions of use
#driver.find_element(By.XPATH, "//a[contains(@href, 'notification_privacy_notice')]" privacy notice
#driver.find_element(By.XPATH, "//a[contains(@href, 'ap/signin')]" sign in

# 2. Create a test case using BDD that opens target.com, clicks on the cart icon and verifies that “Your cart is empty” message is shown
# Located in target_search.feature and target_search.steps.py

# 3.Create a test case using BDD to verify that a logged out user can navigate to Sign In
# Located in target_search.feature and target_search.steps.py