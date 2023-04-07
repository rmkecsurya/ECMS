import time
from selenium.webdriver.common.by import By
from configuration.config import Config as config


class MyProfilePage:
    myProfilePageURL = 'https://staging.epiplex500.com/Settings/AdminEdit.aspx'
    userNameXPath = '//*[@id="ctl00_mainContent_FormView1_TextBox2"]'
    firstNameXPath = '//*[@id="ctl00_mainContent_FormView1_TextBox4"]'
    middleNameXPath = '//*[@id="ctl00_mainContent_FormView1_TextBox5"]'
    lastNameXPath = '//*[@id="ctl00_mainContent_FormView1_TextBox6"]'
    emailIDXPath = '//*[@id="ctl00_mainContent_FormView1_TextBox7"]'
    saveBtnXPath = '//*[@id="ctl00_mainContent_FormView1_btnUpdate"]'
    cancelBtnXPath = '//*[@id="ctl00_mainContent_FormView1_btnCancel"]'
    userName = config.userName
    firstName = config.firstName
    middleName = config.middleName
    lastName = config.lastName
    email = config.email


    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def navigate_to_url(self):
        try:
            self.logger.info("Navigating to the checkout history page")
            self.driver.get(self.myProfilePageURL)
        except Exception as e:
            self.logger.info("Exception occurred in navigating to URL")
            self.logger.info(e)

    def validate_myprofile_page(self):
        try:
            self.logger.info("Validating Myprofile page started")
            # self.driver.find_element(By.XPATH, self.userNameXPath).clear()
            # self.driver.find_element(By.XPATH, self.userNameXPath).send_keys(self.userName)
            self.driver.find_element(By.XPATH, self.firstNameXPath).clear()
            self.driver.find_element(By.XPATH, self.firstNameXPath).send_keys(self.firstName)
            self.driver.find_element(By.XPATH, self.middleNameXPath).clear()
            self.driver.find_element(By.XPATH, self.middleNameXPath).send_keys(self.middleName)
            self.driver.find_element(By.XPATH, self.lastNameXPath).clear()
            self.driver.find_element(By.XPATH, self.lastNameXPath).send_keys(self.lastName)
            self.driver.find_element(By.XPATH, self.emailIDXPath).clear()
            self.driver.find_element(By.XPATH, self.emailIDXPath).send_keys(self.email)
            self.driver.find_element(By.XPATH, self.cancelBtnXPath).click()
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
