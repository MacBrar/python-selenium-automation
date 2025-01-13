from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from Homework_2 import expected_result


@given("Open Target main page")
def open_target_main(context):
    context.driver.get('https://www.target.com/')

@when("User clicks the cart icon")
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'cart?')]").click()
    sleep(2)

@then("Verify “Your cart is empty” is shown")
def verify_your_cart_is_empty(context):
    expected_result = "Your cart is empty"
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    if expected_result == actual_result: print("Test passed")
    else: print("Test failed")
    print(actual_result)

@when("User clicks Sign In, then clicks Sign in again from navigation menu")
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@id='account-sign-in']").click()
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

@then("Verify Sign In form opened")
def verify_sign_in(context):
    expected_result_sign_in = "Sign in with password"
    actual_result_sign_in = context.driver.find_element(By.XPATH, "//button[@id='login']").text
    if expected_result_sign_in == actual_result_sign_in: print("Test passed")
    else: print("Test failed")
    print(actual_result_sign_in)
