import time
import unittest
from selenium.webdriver.common.by import By


class AddNewGroup:
    addNewGroupURL = 'https://staging.epiplex500.com/Groups/CreateGroup.aspx'
    newGroupNameXPath = '//*[@id="ctl00_mainContent_txtGroupName"]'
    newGroupDescription = '//*[@id="ctl00_mainContent_txtGroupDesc"]'
    grpManagerXPath = '//*[@id="ctl00_mainContent_ddlManager"]/option'
    selectMemberXPath = '//*[@id="ctl00_mainContent_gvUsers_ctl02_chkSelect"]'
    multiUserCheckBoxXPath = '//*[@id="ctl00_mainContent_chkMuser"]'
    forceDeactivationCheckBoxXPath = '//*[@id="ctl00_mainContent_chkAutoDeactivate"]'
    askUserForConfirmationXPath = '//*[@id="ctl00_mainContent_chkShowMessageBoxOnDeactivate"]'
    createBtnXPath = '//*[@id="ctl00_mainContent_btnCreate"]'
    cancelBtnXPath = '//*[@id="ctl00_mainContent_btnCancel"]'
    grpAlreadyExistsXPath = '//*[@id="ctl00_mainContent_lblWarningMessage"]'



    def __init__(self, driver,logger):
        self.driver = driver
        self.logger = logger

    def navigate_to_url(self):
        try:
            self.driver.get(self.addNewGroupURL)
            self.logger.info("Navigated to the group Page URL")
        except Exception as e:
            self.logger.info("Exception Occurred in the navigating to the URL")
            self.logger.info(e)
            return False

    def validate_add_group_page(self, newGropName, grpDescription):
        try:
            self.logger.info("Validating the Add Group Page Started")
            self.driver.find_element(By.XPATH, self.newGroupNameXPath).send_keys(newGropName)
            self.driver.find_element(By.XPATH, self.newGroupDescription).send_keys(grpDescription)
            self.driver.find_element(By.XPATH, self.selectMemberXPath).click()
            grpManager = self.driver.find_elements(By.XPATH, self.grpManagerXPath)
            grpManager[1].click()
            self.driver.find_element(By.XPATH, self.multiUserCheckBoxXPath).click()
            self.driver.find_element(By.XPATH, self.forceDeactivationCheckBoxXPath).click()
            askUserConfirmationCheckBox = self.driver.find_element(By.XPATH, self.askUserForConfirmationXPath)
            if askUserConfirmationCheckBox.is_enabled():
                if askUserConfirmationCheckBox.is_selected() == False:
                    self.driver.find_element(By.XPATH, self.askUserForConfirmationXPath).click()
            self.driver.find_element(By.XPATH, self.createBtnXPath).click()
            if(self.driver.find_element(By.XPATH,self.grpAlreadyExistsXPath).text == 'Group name already exists.'):
                self.logger.info("Validating the add group page failed due to Group Already Exists error")
                return False
            else:
                self.logger.info("Group Created Successfully")
                return True
            # for i in range(1, len(grpManager)):
            #     #print(grpManager[i].text)
            #     if grpManager[i].text == 'kumar@epiance':
            #         pass
            #     pass
        except Exception as e:
            self.logger.info("Exception Occurred in the validating the Add group page")
            self.logger.info(e)
            return False