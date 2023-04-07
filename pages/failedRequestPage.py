import time
from selenium.webdriver.common.by import By
from configuration.config import Config as config

class FailedRequestPage:
    checkoutHistoryURL = 'https://staging.epiplex500.com/Reports/Rpt_FailedRequests.aspx'
    selectAllocationStatusXPath = '//*[@id="ctl00_mainContent_DropDownList1"]/option'
    selectAllocationStatusDynamicdata = '//*[@id="ctl00_mainContent_DropDownList1"]/option[{0}]'
    selectAllocationStatusValue = config.selectAllocationStatusValue
    exportToExcel = '//*[@id="ctl00_mainContent_ImgExport"]'

    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    def naviagte_to_url(self):
        try:
            self.logger.info("Navigating to the ")
            self.driver.get(self.checkoutHistoryURL)
        except Exception as e:
            self.logger.info("Exception occurred in navigating to the URL")
            self.logger.infor(e)
            return False
    def validate_failed_request_page(self):
        try:
            selectAllocationStatus = self.driver.find_elements(By.XPATH,self.selectAllocationStatusXPath)
            for i in range(len(selectAllocationStatus)):
                if self.driver.find_element(By.XPATH,self.selectAllocationStatusDynamicdata.format(i+1)).text == self.selectAllocationStatusValue:
                    self.driver.find_element(By.XPATH,self.exportToExcel).click()
                    time.sleep(2)
                    return True
                else:
                    return False
        except Exception as e:
            self.logger.info("Exception occurred in validating the Request page")
            self.logger.info(e)
            return False