import time
from selenium.webdriver.common.by import By

class SignOutPage:
    signOutXpath = '//*[@id="ctl00_SiteMenut25"]'
    successFullMsg = '//*[@id="ctl00_mainContent_LblSuccessFullSignOut"]'

    def staleElements(self,xPath):
        try:
            self.driver.find_element(By.XPATH,xPath)
            return True
        except:
            return False
    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    def Validate_signOut_page(self):
        try:
            self.logger.info("Validating the Signout page Started")
            self.driver.find_element(By.XPATH,self.signOutXpath).click()

            if self.staleElements(self.successFullMsg):
                self.logger.info("Validating the Signout page Successful")
                return True
            else:
                self.logger.info("Validating the Signout page failed")
                return False

        except Exception as e:
            self.logger.info("Exception is signout page")
            self.logger.info(e)
            return False
