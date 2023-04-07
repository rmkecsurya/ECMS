import time
from selenium.webdriver.common.by import By
from configuration.config import Config as config

class ChangePasswordPage:
    changePasswordPageUrl = 'https://staging.epiplex500.com/Settings/ChangePassword.aspx'
    currentPasswordXPath = '//*[@id="ctl00_mainContent_FormView1_TextBox2"]'
    newPasswordXpath = '//*[@id="ctl00_mainContent_FormView1_TextBox4"]'
    confirmPasswordXPath = '//*[@id="ctl00_mainContent_FormView1_TextBox5"]'
    saveBtnXPath ='//*[@id="ctl00_mainContent_FormView1_btnUpdate"]'
    cancelBtnXPath = '//*[@id="ctl00_mainContent_FormView1_btnCancel"]'
    currentPassword = config.currentPassword
    newPassword = config.newPassword

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def navigate_to_url(self):
        try:
            self.logger.info("Navigating to the checkout history page")
            self.driver.get(self.changePasswordPageUrl)
        except Exception as e:
            self.logger.info("Exception occurred in navigating to URL")
            self.logger.info(e)

    def validate_change_password_page(self):
        try:
            self.driver.find_element(By.XPATH,self.currentPasswordXPath).send_keys(self.currentPassword)
            self.driver.find_element(By.XPATH,self.newPasswordXpath).send_keys(self.newPassword)
            self.driver.find_element(By.XPATH,self.confirmPasswordXPath).send_keys(self.newPassword)
            self.driver.find_element(By.XPATH,self.cancelBtnXPath).click()
            if self.driver.title == 'Home- Epiplex License Management System':
                self.logger.info("MyProfile Testcase Passes")
                return True
            else:
                self.logger.info("MyProfile Testcase failed")
                return False
        except Exception as e:
            self.logger.info("Exception occurred in validating the License Utilization page")
            self.logger.info(e)
            return False