from pages.tables import Tables
import time
from selenium.webdriver.common.keys import Keys

def test_webtables_2(browser):
    tables = Tables(browser)
    tables.visit()

    for i in range(2):
        tables.btn_add.click()
        tables.FirstName.send_keys('Child')
        tables.LastName.send_keys('Sweet')
        tables.Email.send_keys('nox@123456.com')
        tables.Age.send_keys('25')
        tables.Salary.send_keys('9000')
        tables.Department.send_keys('IT')
        time.sleep(2)
        tables.submit_btn.click()
        time.sleep(2)

    assert tables.fourLine.get_text() == 'Child'
    assert tables.fiveLine.get_text() == 'Child'

    assert tables.btn_Privious.get_dom_attribute('disabled')
    assert tables.btn_Next.get_dom_attribute('disabled')

    for k in range(3):
        tables.btn_add.click()
        tables.FirstName.send_keys('Child')
        tables.LastName.send_keys('Sweet')
        tables.Email.send_keys('nox@123456.com')
        tables.Age.send_keys('25')
        tables.Salary.send_keys('9000')
        tables.Department.send_keys('IT')
        time.sleep(2)
        tables.submit_btn.click()
        time.sleep(2)

    assert tables.nbr_Pages.get_text() == '2'