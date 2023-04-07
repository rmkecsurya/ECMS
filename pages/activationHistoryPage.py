from selenium.webdriver.common.by import By
import time

class ActivationHistory:
    activationHistoryURL = 'https://staging.epiplex500.com/Reports/Rpt_History.aspx'
    selectActivationHistoryGrpXpath = '//*[@id="ctl00_mainContent_DropDownGroupNames"]/option'
    grpToBeSelect = 'All Groups'
    noRecordFound = '//*[@id="ctl00_mainContent_GridView1"]/tbody/tr/td'
    excelExport = '//*[@id="ctl00_mainContent_ImgExport"]'
    activationHistoryPageDynamicXpath = '//*[@id="ctl00_mainContent_DropDownGroupNames"]/option[{0}]'

    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    def navigate_to_url(self):
        try:
            self.logger.info("Navigating to Activation History URL Page Started")
            self.driver.get(self.activationHistoryURL)
            self.logger.info("Navigating to Activation History URL Page Ended")
        except Exception as e:
            self.logger.info("Exception occurred in navigating to URL")
            self.logger.info(e)
            return False

    def validate_activation_history_page(self):
        self.logger.info("Validating the activation history Page Started")
        try:
            grpList = self.driver.find_elements(By.XPATH,self.selectActivationHistoryGrpXpath)
            for i in range(len(grpList)):
                if grpList[i].text.lower() == self.grpToBeSelect.lower():
                    xPath = self.activationHistoryPageDynamicXpath.format(i+1)
                    self.driver.find_element(By.XPATH,xPath).click()
                    if self.driver.find_element(By.XPATH,self.noRecordFound).text.lower() == 'No records found'.lower():
                        self.logger.info("Validating Activation page failed due to No Records Found Error")
                        return False
                    else:
                        self.driver.find_element(By.XPATH,self.excelExport).click()
                        time.sleep(2)
                    break
            self.logger.info("Validating Activation page successful")
            return True
        except Exception as e:
            self.logger.info("Exception occured in the the validating the activation history page")
            self.logger.info(e)
            return False
