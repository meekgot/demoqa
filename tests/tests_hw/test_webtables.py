from pages.tables import Tables
import time
from selenium.webdriver.common.keys import Keys

def test_webtables(browser):
    tables = Tables(browser)
    tables.visit()

    assert tables.btn_add.visible()
    tables.btn_add.click()
    time.sleep(2)

    assert tables.modal_dialog.visible()
    time.sleep(2)

    tables.submit_btn.click()
    assert tables.validated.exist()

    tables.FirstName.send_keys('Child')
    tables.LastName.send_keys('Sweet')
    tables.Email.send_keys('nox@123456.com')
    tables.Age.send_keys('25')
    tables.Salary.send_keys('9000')
    tables.Department.send_keys('IT')
    time.sleep(2)
    tables.submit_btn.click()
    time.sleep(2)

    assert not tables.modal_dialog.exist()
    time.sleep(2)
    assert tables.fourLine.get_text() == 'Child'
    tables.btn_Edit.click()
    time.sleep(2)
    assert tables.EditModal.exist()
    tables.EditFirstName.click_force()
    tables.EditFirstName.send_keys(Keys.BACKSPACE * 5)
    tables.EditFirstName.send_keys('Baby')
    tables.SubmitEdits.click()
    assert tables.fourLine.get_text() == 'Baby'
    tables.btn_Delete.click()
    assert tables.fourLine.get_text() == ' '