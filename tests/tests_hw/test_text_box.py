from pages.text_box import TextBox
import time

def test_text_box(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()

    send_FullName = 'Sweet Child'
    send_address = 'Saint_Petersburg'

    text_box_page.name.send_keys(send_FullName)
    time.sleep(2)
    text_box_page.current_address.send_keys(send_address)
    time.sleep(2)
    text_box_page.btn_submit.click()

    assert (text_box_page.output.get_text() == 'Name:' + send_FullName+ "\n" + 'Current Address :' + send_address)