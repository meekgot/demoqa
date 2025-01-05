import time

from pages.links import Links


def test_window_tab(browser):
    links = Links(browser)
    links.visit()

    assert links.Home_link.exist()
    assert links.Home_link.get_text() == "Home"
    assert links.Home_link.get_dom_attribute('href') == 'https://demoqa.com'

    links.Home_link.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2
