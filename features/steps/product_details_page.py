from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import re


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Blue Tint', 'Denim Blue', 'Raven', 'Marine']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

COLORS_DIV = (By.CSS_SELECTOR, "div[data-module-type='ProductDetailVariationSelector']")
COLORS = (By.CSS_SELECTOR, "picture img[height='64px'][width='64px']")
SELECTED_COLOR = (By.CSS_SELECTOR, "div[class*='styles_headerWrapper']")

@then("click colors and verify")
def click_and_verify(context):
    expected_colors = ['Medium Wash', 'Khaki', 'Light Blue']
    context.driver.wait.until(EC.visibility_of_element_located(COLORS_DIV))
    colors = context.driver.find_elements(*COLORS)
    sleep(10)  ## popups keep coming up and it screws with clicks

    for color in colors:
        context.driver.wait.until(EC.element_to_be_clickable(color))
        color.click()
        color_text = context.driver.find_element(*SELECTED_COLOR).text
        color_text_formatted = re.sub(r'Color.*\n', '', color_text)
        assert str(
            color_text_formatted) in expected_colors, f"actual: {color_text_formatted} not in expected colors: {expected_colors}"

@given("Open target jeans")
def open_main(context):
    context.driver.get('www.target.com/p/men-s-big-tall-athletic-fit-jeans-goodfellow-co/-/A-81898360?preselect=80818468#lnk=sametab')