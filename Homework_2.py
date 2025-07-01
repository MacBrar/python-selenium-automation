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

# Part 1: Locators for Amazon Sign in page
#driver.find_element(By.XPATH, "//i[@aria-label='Amazon']") amazon logo
#driver.find_element(By.XPATH, "//input[@type='email']") email field
#driver.find_element(By.XPATH, "//input[@id='continue']") continue button
#driver.find_element(By.XPATH, "//a[contains(text(),'Conditions')]") conditions of use
#driver.find_element(By.XPATH, "//a[contains(text(),'Privacy')]") privacy notice
#driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']") need help
#driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']") forgot your password
#driver.find_element(By.XPATH, "//a[contains(text(),'Other issues')]") other issues with sign in
#driver.find_element(By.XPATH, "//a[contains(text(),'Create your')]") create your account button

# Part 2: Create a test case for sign-in page
# open the url
driver.get('https://www.target.com/')
sleep(2)
driver.find_element(By.ID,"account-sign-in").click()
sleep(2)
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(2)
expected_result = "Sign in or create account"
actual_result= driver.find_element(By.XPATH, "//*[text()='Sign in or create account']").text
assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
print('Test case passed')

driver.quit()