import time
from selenium.webdriver.common.by import By
from configuration.config import Config as config

class CheckoutStatusPage:
    checkoutStatusPageURL = 'https://staging.epiplex500.com/Reports/Rpt_OfflineActivation.aspx'
    norecordFoundError = '//*[@id="ctl00_mainContent_GridView1"]/tbody/tr/td'
    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    def stale_elements(self,xpath):
        try:

            if self.driver.get_element(By.XPATH,xpath).text == 'No records found':
                return True
            else:
                return False
        except:
            return False

    def navigate_to_url(self):
        try:
            self.logger.info("Navigating to the StatusReport page URL")
            self.driver.get(self.checkoutStatusPageURL)
        except Exception as e:
            self.logger.info("Exception occurred in Navigating to the Staus page URL")
            self.logger.info(e)
            return False

    def validate_checkout_status_page(self):
        try:
            if not self.driver.find_element(By.XPATH,self.norecordFoundError).text == 'No records found':
                print("Displayed")
                return True
            else:
                print("Not displayed")
                return False
        except Exception as e:
            self.logger.info("Exception occurred in validating the checkout status page")
            self.logger.info(e)
            return False
