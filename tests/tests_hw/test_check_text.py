from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
#
# def test_check_text_footer(browser):
#     demo_qa_page = DemoQa(browser)
#     demo_qa_page.visit()
#     current_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
#     assert demo_qa_page.text_elements.get_text() == current_text
#
#
# def test_check_text(browser):
#     demo_qa_page = DemoQa(browser)
#     demo_qa_page.visit()
#     demo_qa_page.btn_elements.click()
#     current_text_elements = 'Please select an item from left to start practice.'
#     assert demo_qa_page.text_class.get_text() == current_text_elements

# def test_page_elements(browser):
#     el_page = ElementsPage(browser)
#
#     el_page.visit()
#     assert el_page.text_elements.get_text() == 'Please select an item from left to start practice.'

def test_page_elements(browser):
    el_page = ElementsPage(browser)

    el_page.visit()
    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_texbox.exist()