import time
from pages.alert import Alert


def test_check_alert(browser):
    alert_page = Alert(browser)
    alert_page.visit()

    alert_page.timer_alert.click()
    time.sleep(6)
    assert alert_page.alert()