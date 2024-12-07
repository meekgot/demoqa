from pages.accordion import Accordian
import time


def test_visible_accordion(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert accordian_page.btn_accordian.visible()
    accordian_page.heading.click()
    time.sleep(2)
    assert not accordian_page.btn_accordian.visible()

def test_visible_accordian_default(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert not accordian_page.element1.visible()
    assert not accordian_page.element2.visible()
    assert not accordian_page.element3.visible()