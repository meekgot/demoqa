from pages.modal_dialogs import ModalDialogs
from selenium.webdriver.common.keys import Keys
import time

def test_check_modal_dialogs(browser):
    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()

    assert modal_dialogs_page.SmallModalButton.exist()
    assert modal_dialogs_page.LargeModalButton.exist()

    modal_dialogs_page.SmallModalButton.click()
    assert modal_dialogs_page.ModalSmallWindow.get_text() == 'Small Modal'
    time.sleep(2)
    modal_dialogs_page.close_btn_Small.click()
    time.sleep(2)

    modal_dialogs_page.LargeModalButton.click()
    assert modal_dialogs_page.ModalLargeWindow.get_text() == 'Large Modal'
    time.sleep(2)
    modal_dialogs_page.close_btn_Large.click()
    time.sleep(2)