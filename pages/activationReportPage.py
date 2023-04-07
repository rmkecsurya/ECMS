from selenium.webdriver.common.by import By
import time

class ActivatePage:
    activatePageURL='https://staging.epiplex500.com/Reports/RPT_Activation.aspx'
    groupdropXpath = '//*[@id="ctl00_mainContent_DropDownList1"]/option'
    groupName = "PDC"
    clickprint = '//*[@id="ctl00_mainContent_ImgPrint"]'
    clickcsv = '//*[@id="ctl00_mainContent_ImgExport"]'
    activationReportPageDynamicXpath = '//*[@id="ctl00_mainContent_DropDownList1"]/option[{0}]'

    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger
    def navigate_to_URL(self):
        try:
            self.logger.info("Navigating to Activation Report Page started")
            self.driver.get(self.activatePageURL)
            self.logger.info("Navigating to Activation Report Page Ended")
        except Exception as e:
            self.logger.info("Exception occurred in the activation report URL page")
            self.logger.info(e)
            return False

    def validate_activation_report_page(self):
        try:
            self.logger.info("Validating the activation report page Started")
            allocation = self.driver.find_elements(By.XPATH, self.groupdropXpath)
            for index in range(len(allocation)):
                if allocation[index].text.lower() == self.groupName.lower():
                    xPath = self.activationReportPageDynamicXpath.format(index + 1)
                    self.driver.find_element(By.XPATH, xPath).click()
                    self.driver.find_element(By.XPATH, self.clickcsv).click()
                    time.sleep(2)
                    self.logger.info("Exporting CSV tested in the Activation page")
                    return True

        except:
            self.logger.info("Exception occured in validating the ActivationPage")
            return False