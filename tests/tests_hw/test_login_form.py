import time
from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys

def test_state_and_city(browser):
    form_page = FormPage(browser)
    form_page.visit()

    form_page.State.scroll_to_element()
    time.sleep(3)
    form_page.State_input.click_force()
    time.sleep(3)
    form_page.State_input.send_keys(Keys.DOWN * 4)
    time.sleep(3)
    form_page.State_input.send_keys(Keys.ENTER)
    time.sleep(10)
    form_page.City_input.click_force()
    time.sleep(5)
    form_page.City_input.send_keys(Keys.DOWN * 2)
    time.sleep(2)
    form_page.City_input.send_keys(Keys.ENTER)
    time.sleep(10)