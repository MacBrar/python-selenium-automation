from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@then('Verify search results shown')
def verify_search_results(context):
    expected_result = 'tea'
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.ID,"account-sign-in").click()
    sleep(2)

@then("From right side navigation menu, click Sign In")
def nav_menu_signin(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(2)

@then("Verify Sign In form opened")
def verify_signin_form(context):
    expected_result = "Sign in or create account"
    actual_result = context.driver.find_element(By.XPATH, "//*[text()='Sign in or create account']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
    print('Test case passed')

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(10)

@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected text {product} not in actual {actual_result}'

