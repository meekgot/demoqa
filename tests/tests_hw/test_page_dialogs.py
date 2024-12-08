from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa
import time

# def test_modal_elements(browser):
#     modal_dialogs_page = ModalDialogs(browser)
#     modal_dialogs_page.visit()
#     assert modal_dialogs_page.modal_elements.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()
    modal_dialogs_page.refresh()
    modal_dialogs_page.main_icon.click()
    time.sleep(2)
    browser.back()
    time.sleep(2)
    browser.set_window_size(900, 400)
    time.sleep(2)
    browser.forward()

    demo_qa_page = DemoQa(browser)
    assert demo_qa_page.equal_url()
    assert browser.title == "DEMOQA"

    browser.set_window_size(1000, 1000)