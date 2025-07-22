from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target circle main page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify {expected_amount} header links are shown')
def verify_header_links_amount(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind elements:')
    print(links)
    print(type(len(links)))

    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'