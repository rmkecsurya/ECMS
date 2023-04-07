import time
from selenium.webdriver.common.by import By
class LoginPage:
    url = 'https://staging.epiplex500.com/'
    usernameXPath = '//*[@id="ctl00_mainContent_txtUserName"]'
    passwordXPath = '//*[@id="ctl00_mainContent_txtPassword"]'
    btnPath = '//*[@id="ctl00_mainContent_LoginButton"]'
    def __init__(self,driver,username,password,logger):
        #super.__init__(self,driver)
        self.driver = driver
        self.username = username
        self.password = password
        self.logger = logger

    def navigate_to_url(self):
        try:
            self.driver.get(self.url)
            self.logger.info("Navigated to LoginPage URL")
        except Exception as e:
            self.logger.info("Exception occured in navigating the URL")
            self.logger.info(e)
            return False
    def validate_login(self):
        try:
            self.driver.find_element(By.XPATH,self.usernameXPath).send_keys(self.username)
            self.driver.find_element(By.XPATH,self.passwordXPath).send_keys(self.password)
            self.driver.find_element(By.XPATH, self.btnPath).click()
            self.logger.info("SuccessFully Validatd the LoginPage")
            return True

        except Exception as e:
            self.logger.info("Exception occured in validating the Login page")
            self.logger.info(e)
            return False


