from selenium.webdriver.common.by import By
from pages.addNewGroup import AddNewGroup
from configuration.config import Config as config


class GroupPage:
    grpPageURL='https://staging.epiplex500.com/Groups/Groups.aspx'
    addNewGrpBtnXpath = '//*[@id="ctl00_mainContent_btnNewGroup_top"]'
    grpTableXpath = '//*[@id="ctl00_mainContent_gvGroups"]/tbody/tr/td[2]'
    grpEditBtnXPath = '//*[@id="ctl00_mainContent_gvGroups"]/tbody/tr/td[5]/input'
    grpDeleteBtnXPath = '//*[@id="ctl00_mainContent_gvGroups"]/tbody/tr/td[6]/input'
    changeDescXPath = '//*[@id="ctl00_mainContent_fvEditGroup_txtGroupDesc"]'
    membersXpath = '//*[@id="ctl00_mainContent_fvEditGroup_gvUsers_ctl03_chkSelect"]'
    grpEditManagerXPath = '//*[@id="ctl00_mainContent_fvEditGroup_ddlManager"]/option[2]'
    multiUserCheckBoxXPath = '//*[@id="ctl00_mainContent_fvEditGroup_chkMuser"]'
    forceDeactivationCheckBoxXPath = '//*[@id="ctl00_mainContent_fvEditGroup_chkAutoDeactivate"]'
    askUserForConfirmationXPath = '//*[@id="ctl00_mainContent_fvEditGroup_chkShowAutoDeactivateMessage"]'
    updateBtnXpath = '//*[@id="ctl00_mainContent_fvEditGroup_ImageButton1"]'
    cancelBtnXPath = '//*[@id="ctl00_mainContent_fvEditGroup_ImageButton2"]'
    searchTxtBoxXPath = '//*[@id="ctl00_mainContent_txtSearch"]'
    searchBtnXPath = '//*[@id="ctl00_mainContent_btnSearch"]'
    noRecordFoundErrorXpath = '//*[@id="ctl00_mainContent_gvGroups"]/tbody/tr/td'

    groupName = config.groupName
    toBeSearched = config.toBeSearched
    grpDescription = config.grpDescription
    grpDetailsToBeChanged = config.grpDetailsToBeChanged

    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger
    def navigate_toURL(self):
        self.driver.get(self.grpPageURL)

    def validate_add_new_groupPage(self):
        try:
            self.logger.info("Validating the Add new group page started")
            addNewGroupObj = AddNewGroup(self.driver, self.logger)
            addNewGroupObj.navigate_to_url()
            grpCreationResult = addNewGroupObj.validate_add_group_page(self.groupName, self.grpDescription)
            if grpCreationResult:
                self.logger.info("Validating the Add new group page Successful")
                return True
            else:
                self.logger.info("Validating the Add new group page Failed")
                return False
        except Exception as e:
            self.logger.info("Exception occurred in Add new GroupPage")
            self.logger.info(e)
            return False

    def validate_edit_groupPage(self):
        try:
            self.logger.info("Validating the edit group page started")
            groups = self.driver.find_elements(By.XPATH, self.grpTableXpath)
            for i in range(0, len(groups)):
                if groups[i].text == self.grpDetailsToBeChanged:
                    self.driver.find_element(By.XPATH, self.grpEditBtnXPath).click()
                    self.driver.find_element(By.XPATH, self.changeDescXPath).clear()
                    self.driver.find_element(By.XPATH, self.changeDescXPath).send_keys("Change in the description")
                    self.driver.find_element(By.XPATH, self.membersXpath).click()
                    # self.driver.find_element(By.XPATH,self.grpEditMemberXpath).click()
                    self.driver.find_element(By.XPATH, self.multiUserCheckBoxXPath).click()
                    self.driver.find_element(By.XPATH, self.forceDeactivationCheckBoxXPath).click()
                    askUserConfirmationCheckBox = self.driver.find_element(By.XPATH, self.askUserForConfirmationXPath)
                    if askUserConfirmationCheckBox.is_enabled():
                        if askUserConfirmationCheckBox.is_selected() == False:
                            self.driver.find_element(By.XPATH, self.askUserForConfirmationXPath).click()
                    self.driver.find_element(By.XPATH, self.updateBtnXpath).click()
                    # self.driver.find_element(By.XPATH,self.cancelBtnXPath).click()
                    if self.driver.title == 'Groups':
                        self.logger.info("Validating the edit group page successful")
                        return True
                    else:
                        self.logger.info("Validating the edit group page failed")
                        return False
            else:
                self.logger.info("Group Doesn't Exists")
                return False
        except Exception as e:
            self.logger.info("Exception occurred in Edit Group Page")
            self.logger.info(e)
            return False


    def validate_delete_group(self):
        try:
            self.logger.info("Validating the delete group page started")
            groups = self.driver.find_elements(By.XPATH, self.grpTableXpath)
            for i in range(0, len(groups)):
                if groups[i].text == self.grpDetailsToBeChanged:
                    self.driver.find_element(By.XPATH, self.grpDeleteBtnXPath).click()
                    self.driver.switch_to.alert.accept()
                    self.logger.info("Validating the delete group page successful")
                    return True
            else:
                self.logger.info("Validating the delete group page failed")
                return False
        except Exception as e:
            self.logger.info("Exception occurred in Deleting the group page")
            self.logger.info(e)
            return False

    def validate_search_group(self):
        try:
            self.logger.info("Validating the Search group page started")
            self.driver.find_element(By.XPATH, self.searchTxtBoxXPath).send_keys(self.toBeSearched)
            self.driver.find_element(By.XPATH, self.searchBtnXPath).click()
            if self.driver.find_element(By.XPATH,self.noRecordFoundErrorXpath).text == "No Record Found":
                self.logger.info("NoRecordFound")
                return False
            else:
                self.logger.info("Validating the Search group page successfull")
                return True
        except Exception as e:
            self.logger.info("Exception occurred in Searching the group")
            self.logger.info(e)
            return False

