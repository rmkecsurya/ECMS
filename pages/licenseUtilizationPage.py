import time
from selenium.webdriver.common.by import By
from configuration.config import Config as config


class LicenseUtilizationPage:
    licenseUtilizationPageURL = 'https://staging.epiplex500.com/Reports/Rpt_LicUsage.aspx'
    fromDateXpath = '//*[@id="ctl00_mainContent_txtStartDate"]'
    toDateXpath = '//*[@id="ctl00_mainContent_txtEndDate"]'
    selectProductComboboxXPath = '//*[@id="ctl00_mainContent_DropDownList1"]/option'
    selectProductComboboxDynamicXPath = '//*[@id="ctl00_mainContent_DropDownList1"]/option[{0}]'
    noRecordFoundXPath = '//*[@id="ctl00_mainContent_GridView1"]/tbody/tr/td'
    excelExport = '//*[@id="ctl00_mainContent_ImgExport"]'
    fromDate = config.fromDate
    toDate = config.toDate
    selectProduct = config.selectProduct

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def navigate_to_url(self):
        try:
            self.logger.info("Navigating to the checkout history page")
            self.driver.get(self.licenseUtilizationPageURL)
        except Exception as e:
            self.logger.info("Exception occurred in navigating to URL")
            self.logger.info(e)

    def validate_license_utilization_page(self):
        try:
            self.logger.info("Validating the license utilization page started")
            self.driver.find_element(By.XPATH,self.fromDateXpath).clear()
            self.driver.find_element(By.XPATH,self.fromDateXpath).send_keys(self.fromDate)
            self.driver.find_element(By.XPATH,self.toDateXpath).clear()
            self.driver.find_element(By.XPATH,self.toDateXpath).send_keys(self.toDate)
            products = self.driver.find_elements(By.XPATH,self.selectProductComboboxXPath)
            for i in range(len(products)):
                if self.driver.find_element(By.XPATH,self.selectProductComboboxDynamicXPath.format(i+1)).text == self.selectProduct:
                    self.driver.find_element(By.XPATH,self.selectProductComboboxDynamicXPath.format(i+1)).click()
                    if(self.driver.find_element(By.XPATH,self.noRecordFoundXPath).text == 'No records found'):
                        self.logger.info("Testcase Failed due to No Record Found Error ")
                        return False
                    else:
                        self.driver.find_element(By.XPATH,self.excelExport).click()
                        return True

        except Exception as e:
            self.logger.info("Exception occurred in validating the License Utilization page")
            self.logger.info(e)
            return False
