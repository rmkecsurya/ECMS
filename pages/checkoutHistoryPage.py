import time
from selenium.webdriver.common.by import By
from configuration.config import Config as config


class CheckOutHistoryPage:
    checkoutHistoryURL = 'https://staging.epiplex500.com/Reports/Rpt_CheckoutHistory.aspx'
    selectProductComboBox = '//*[@id="ctl00_mainContent_DropDownList1"]/option'
    selectProductComboBoxDynamicdata = '//*[@id="ctl00_mainContent_DropDownList1"]/option[{0}]'
    noRecordFoundXPath = '//*[@id="ctl00_mainContent_GridView1"]/tbody/tr/td'
    excelExportXPath = '//*[@id="ctl00_mainContent_ImgExport"]'
    checkoutHistorySelectProduct = config.checkoutHistorySelectProduct

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def navigate_to_url(self):
        try:
            self.logger.info("Navigating to the checkout history page")
            self.driver.get(self.checkoutHistoryURL)
        except Exception as e:
            self.logger.info("Exception occurred in navigating to URL")
            self.logger.info(e)

    def validate_checkout_history_page(self):
        try:
            self.logger.info("Validating the history page started")
            selectProduct = self.driver.find_elements(By.XPATH, self.selectProductComboBox)
            for i in range(len(selectProduct)):
                if self.driver.find_element(By.XPATH,self.selectProductComboBoxDynamicdata.format(i + 1)).text == self.checkoutHistorySelectProduct:
                    self.driver.find_element(By.XPATH, self.selectProductComboBoxDynamicdata.format(i + 1)).click()
                    if self.driver.find_element(By.XPATH, self.noRecordFoundXPath).text == 'No records found':
                        self.logger.info("TestCase Failed due to No record found")
                        return False
                    else:
                        self.logger.info("Record found and exporting to Excel")
                        self.driver.find_element(By.XPATH, self.excelExportXPath).click()
                        time.sleep(2)
                        return True
        except Exception as e:
            self.logger.info("Exception occurred in validating the checkout history page")
            self.logger.info(e)
            return False
