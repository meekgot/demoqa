from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement

class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, 'span[title="Delete"]')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.FirstName = WebElement(driver, '#firstName')
        self.LastName = WebElement(driver, '#lastName')
        self.Email = WebElement(driver, '#userEmail')
        self.Age = WebElement(driver, '#age')
        self.Salary = WebElement(driver, '#salary')
        self.Department = WebElement(driver, '#department')
        self.submit_btn = WebElement(driver,'#submit')
        self.Exit = WebElement(driver, 'body > div.fade.modal.show > div > div > div.modal-header > button > span:nth-child(1)')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.validated = WebElement(driver, '#userForm.was-validated')
        self.fourLine = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.btn_Edit = WebElement(driver, '#edit-record-4 > svg > path')
        self.EditModal = WebElement(driver, 'body > div.fade.modal.show > div > div > div.modal-header')
        self.EditFirstName = WebElement(driver, '#firstName')
        self.SubmitEdits = WebElement(driver, '#userForm > div.mt-4.justify-content-end.row > div')
        self.btn_Delete = WebElement(driver, '#delete-record-4 > svg > path')
        self.fiveLine = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(5) > div > div:nth-child(1)')
        self.btn_Privious = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')
        self.btn_Next = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.nbr_Pages = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > span')
