from pages.tables import Tables
import time


def test_sort(browser):
    tables = Tables(browser)
    tables.visit()

    tables._FirstName.click_force()
    assert tables.sort_FirstName.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    tables._LastName.click_force()
    assert tables.sort_LastName.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    tables._Age.click_force()
    assert tables.sort_Age.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    tables._Email.click_force()
    assert tables.sort_Email.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(2)

    tables._Salary.click_force()
    assert tables.sort_Salary.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    time.sleep(3)

    tables._Department.click_force()
    time.sleep(2)
    assert tables.sort_Department.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'