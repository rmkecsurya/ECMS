import time
from selenium.webdriver.common.by import By
from configuration.config import Config as config

class ForceDeactivatingPage:
    forceDeactivationStatusComboboxXPath = '//*[@id="ctl00_mainContent_DropDownList1"]/option'
    forceDeactivationStatusComboboxDynamicXPath = '//*[@id="ctl00_mainContent_DropDownList1"]/option[{0}]'
    forceDeactivatePageURL = 'https://staging.epiplex500.com/Reports/Rpt_IncompleteActivation.aspx'
    forceDeactivationStatus = config.forceDeactivationStatus
    noRecordFoundXPath = '//*[@id="ctl00_mainContent_GridFailedActivation"]/tbody/tr/td'
    excelExportXPath = '//*[@id="ctl00_mainContent_ImgExport"]'
    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    def navigate_to_url(self):
        try:
            self.logger.info("Navigating to the URL")
            self.driver.get(self.forceDeactivatePageURL)
        except Exception as e:
            self.logger.info("Exception occurred in navigating to url")
            self.logger.info(e)
            return False

    def validate_force_deactivation_page(self):
        try:
            self.logger.info("Validating the force deactivation page started")
            license = self.driver.find_elements(By.XPATH,self.forceDeactivationStatusComboboxXPath)
            if not self.driver.find_element(By.XPATH, self.noRecordFoundXPath).text == 'No records found':
                for i in range(len(license)):
                    if self.driver.find_element(By.XPATH, self.forceDeactivationStatusComboboxDynamicXPath.format(i + 1)).text == self.forceDeactivationStatus:
                        self.driver.find_element(By.XPATH, self.forceDeactivationStatusComboboxDynamicXPath.format(i + 1)).click()
                    else:
                        self.logger.info("Record found and exporting to Excel")
                        self.driver.find_element(By.XPATH, self.excelExportXPath).click()
                        time.sleep(2)
                        return True
            else:
                self.logger.info("TestCase failed due to No Record Found Error")
                return False

        except Exception as e:
            self.logger.info("Exception occurred in validating the checkout history page")
            self.logger.info(e)
            return False
