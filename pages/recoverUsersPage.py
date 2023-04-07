import time
from selenium.webdriver.common.by import By

class RecoverUserPage:
    toBeRecovered = 'Ultimate'
    recoveryPageUrl = 'https://staging.epiplex500.com/Users/UndoDeleteUser.aspx'
    searchTxtBoxXPath = '//*[@id="ctl00_mainContent_TextBox1"]'
    usersTableXPath = '//*[@id="ctl00_mainContent_GridView1"]/tbody/tr/td[2]'
    noRecordFound = '//*[@id="ctl00_mainContent_GridView1"]/tbody/tr/td'
    searchBtnXPath = '//*[@id="ctl00_mainContent_btnSearch"]'
    cancelBtnXPath = '//*[@id="ctl00_mainContent_btnClear"]'
    recoveryBtnXPath = '//*[@id="ctl00_mainContent_btnRecover2"]'

    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    def navigate_to_url(self):
        try:
            self.logger.info("Navigating to URL")
            self.driver.get(self.recoveryPageUrl)
        except Exception as e:
            self.logger.info("Exception occurred in navigating the URL")
            self.logger.info(e)
            return False

    def validate_recovery_search(self):
        try:
            self.logger.info("Validating the Search for the Recovery User Page Started")
            self.driver.find_element(By.XPATH, self.searchTxtBoxXPath).send_keys(self.toBeRecovered)
            self.driver.find_element(By.XPATH, self.searchBtnXPath).click()
            if self.driver.find_element(By.XPATH, self.noRecordFound).text == 'No Records found':
                self.logger.info("Validating the Search for the Recovery User Page Failed")
                return False
            else:
                self.logger.info(self.toBeRecovered + " User found in the recover list")
                return True
        except Exception as e:
            self.logger.info("Exception occurred in searching for the recovery User")
            self.logger.info(e)

    def validate_recovery_page(self):
        try:
            self.logger.info("Validating the Recovery Page Started")
            self.driver.find_element(By.XPATH, self.searchTxtBoxXPath).send_keys(self.toBeRecovered)
            self.driver.find_element(By.XPATH, self.searchBtnXPath).click()
            if self.driver.find_element(By.XPATH, self.noRecordFound).text == 'No Records found':
                self.logger.info("No Record Found")
                return False
            else:
                users = self.driver.find_elements(By.XPATH, self.usersTableXPath)
                self.logger.info("Record Found")
                for i in range(0, len(users)):
                    print(users[i].text)
                    if users[i].text == self.toBeRecovered:
                        usersCheckBoxXPath = '//*[@id="ctl00_mainContent_GridView1"]/tbody/tr[{0}]/td[1]/input'.format(
                            i + 2)
                        self.driver.find_element(By.XPATH, usersCheckBoxXPath).click()
                        self.driver.find_element(By.XPATH, self.recoveryBtnXPath).click()
                        time.sleep(5)
                        return True
        except Exception as e:
            self.logger.info("Exception occurred in Recovery User Page")
            self.logger.info(e)
            return False