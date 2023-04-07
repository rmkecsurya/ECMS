import time
from selenium.webdriver.common.by import By

from configuration.config import Config


class AllocationReportPage:
    allocationPageURL = 'https://staging.epiplex500.com/Reports/Rpt_Allocation.aspx'
    allocationStatus = Config.SelectAllocationStatus
    selectProduct = Config.SelectProduct
    selectAllocationXPath = '//*[@id="ctl00_mainContent_DropDownList1"]/option'
    selectProductXPath = '//*[@id="ctl00_mainContent_DropDownProducts"]/option'
    noRecordFundXPath = '//*[@id="ctl00_mainContent_GridFailedActivation"]/tbody/tr/td'
    excelExport = '//*[@id="ctl00_mainContent_ImgExport"]'
    allocationPageDynamicXPath = '//*[@id="ctl00_mainContent_DropDownList1"]/option[{0}]'
    allocationPageSelectProductXPath = '//*[@id="ctl00_mainContent_DropDownProducts"]/option[{0}]'


    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    def stale_elements(self,xPath):
        try:
            if self.driver.find_element(By.XPATH,xPath).text == 'No records found':
                return True
        except:
            return False


    def navigate_to_url(self):
        try:
            self.logger.info("Navigate to Allocation Page URL started")
            self.driver.get(self.allocationPageURL)
            self.logger.info("Navigate to Allocation Page URL Ended")
        except Exception as e:
            self.logger.info("Exception in Navigating to URL")
            self.logger.info(e)

    def validate_allocation_page(self):
        try:
            self.logger.info("Validating Allocation Page Started")
            allocation = self.driver.find_elements(By.XPATH,self.selectAllocationXPath)
            for index in range(len(allocation)):
                if allocation[index].text.lower() == self.allocationStatus.lower():
                    xPath = self.allocationPageDynamicXPath.format(index+1)
                    self.driver.find_element(By.XPATH,xPath).click()
                    #time.sleep(15)
                    break

            selectProduct = self.driver.find_elements(By.XPATH,self.selectProductXPath)
            for index in range(len(selectProduct)):
                if selectProduct[index].text.lower() == self.selectProduct.lower():
                    xPath = self.allocationPageSelectProductXPath.format(index+1)
                    self.driver.find_element(By.XPATH,xPath).click()
                    #time.sleep(15)
                    break
            noRecordFound = self.stale_elements(self.noRecordFundXPath)
            if noRecordFound:
                self.logger.info("No records Found in Allocation reports Page")
                return False
            else:
                self.logger.info("Records Found")
                self.driver.find_element(By.XPATH,self.excelExport).click()
                time.sleep(2)
                return True

        except Exception as e:
            self.logger.info("Exception in Validating the Allocation Page")
            self.logger.info(e)
            return False