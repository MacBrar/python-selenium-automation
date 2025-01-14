from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target Circle main page")
def open_target_circle(context):
    context.driver.get("https://www.target.com/circle")

@when("Open Target Circle main page is opened")
def target_circle_sleep(context):
    sleep(2)

@then("Verify there are at least 10 benefit cells")
def verify_how_many_cells(context):
    benefit_cells = context.driver.find_elements(By.XPATH, "//div[@class='sc-731b5840-5 jeWtiw']")
    print("Benefit cells: ", benefit_cells)

    if len(benefit_cells) >= 10: print("Test passed")
    else: print("Test failed")

@when("Search for {search_word}")
def search_for_word(context, search_word):
    search = context.driver.find_element(By.XPATH, "//input[@id='search']").clear()
    search.send_keys(search_word)
    sleep(2)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(2)

@then("Item can be added to cart")
def add_to_cart(context):
    context.driver.find_element(By.XPATH, "//button[contains(@id,'addToCartButton')]").click() #add to cart after search
    sleep(2)
    context.driver.find_element(By.XPATH, "//div[@data-test='content-wrapper']//button[contains(@id,'addToCartButton')]']").click() #add to cart from side menu
    sleep(2)
    cart_confirmation = context.driver.find_element(By.XPATH, "//div[@class='sc-b5d0650b-2 gSvPkw]").text
    if cart_confirmation == "Added to cart": print("Test passed")
    else: print("Test failed")