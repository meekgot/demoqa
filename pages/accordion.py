from components.components import WebElement
from pages.base_page import BasePage


class Accordian(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.btn_accordian = WebElement(driver, '#section1Content > p')
        self.heading = WebElement(driver, '#section1Heading')
        self.element1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.element2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.element3 = WebElement(driver, '#section3Content > p')