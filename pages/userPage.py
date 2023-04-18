import time
from selenium.webdriver.common.by import By
from configuration.config import Config as config
from pages.addNewUser import AddNewUser



class UserPage:

    usersUrl = 'https://staging.epiplex500.com/Users/Users.aspx'
    newUserURL = 'https://staging.epiplex500.com/Users/CreateUser.aspx'
    searchTextBoxPath = '//*[@id="ctl00_mainContent_txtSearch"]'
    usersListXPath = '//*[@id="ctl00_mainContent_gvUsers"]/tbody/tr/td[2]'
    searchXpath = '//*[@id="ctl00_mainContent_btnSearch"]'
    addNewUserXPath = '//*[@id="ctl00_mainContent_HyperLink2"]/img'
    editUserNameXPath = '//*[@id="ctl00_mainContent_FormView1_txtUsername"]'
    editAccessKeyXPath = '//*[@id="ctl00_mainContent_FormView1_txtAccesskey"]'
    editFullNameXPath = '//*[@id="ctl00_mainContent_FormView1_txtName"]'
    editEmailXPath = '//*[@id="ctl00_mainContent_FormView1_txtEmail"]'
    updateUserXpath = '//*[@id="ctl00_mainContent_FormView1_btnEditUser"]'
    usersListXpath = '//*[@id="ctl00_mainContent_gvUsers"]/tbody/tr/td[2]'
    noRecordsForNew = '//*[@id="ctl00_mainContent_gvUsers"]/tbody/tr/td'
    userEditError = '//*[@id="tableMessage"]/tbody'
    editUserDynamicXpath = '//*[@id="ctl00_mainContent_gvUsers"]/tbody/tr[{0}]/td[8]/input'
    userToBeSearched = config.userToBeSearched
    userToBeEdited = config.userToBeEdited
    userToBeDeleted = config.userToBeDeleted

    def __init__(self, driver,logger):
        self.driver = driver
        self.logger = logger

    def getStaleElement(self,xPath):
        try:
            self.driver.find_element(By.XPATH, xPath)
            return True
        except:
            return False

    #Validating the UserPage
    def validate_add_new_user(self):
        try:
            self.logger.info("Validating Add New User Page started")
            # print("Adding the new user")
            userName = config.addNewUser_name
            accessKey = config.addNewUser_accessKey
            fullName = config.addNewUser_fullName
            emailId = config.addNewUser_emailId
            addNewUser = AddNewUser(self.driver, self.newUserURL,self.logger)
            addNewUser.navigate_toURL()
            isUserCreationSuccessFull = addNewUser.newUserCreateion(userName, accessKey, fullName, emailId)
            if isUserCreationSuccessFull:
                self.logger.info("Validating New User Page Successful")
                return True

            else:
                self.logger.info("New UserPage Validation is not successful")
                return False
        except Exception as e:
            self.logger.info("Exception raised in Validating the add new user Page")
            self.logger.info(e)
            return False

    #Validating the SearchUser
    def validate_search_user(self):
        try:
            self.logger.info("Searching for the user Started")
            self.driver.get(self.usersUrl)
            self.logger.info("Navigated to the User search page")
            self.driver.find_element(By.XPATH, self.searchTextBoxPath).send_keys(self.userToBeSearched)
            # userList = self.driver.find_elements(By.XPATH, self.usersListXPath)
            # print("The total number of users are " + str(len(userList)))
            self.driver.find_element(By.XPATH, self.searchXpath).click()
            time.sleep(5)
            if self.driver.find_element(By.XPATH, self.noRecordsForNew).text == 'No Record Found':
                self.logger.info("User Not Found")
                return False
            else:
                self.logger.info("User Found")
                return True
        except Exception as e:
            self.logger.info("Exception occurred in validating the search user page")
            self.logger.info(e)
            return False

    def validate_edit_user_page(self):
        try:
            self.logger.info("Editing the User Page Started")
            userName = config.editUser_userName
            accessKey = config.editUser_accessKey
            fullName = config.editUser_fullName
            emailId = config.editUser_emailId

            self.driver.get(self.usersUrl)
            self.logger.info("Navigated to the User URL Page")
            userList = self.driver.find_elements(By.XPATH, self.usersListXpath)
            for i in range(1, len(userList)):
                if userList[i].text.lower() == self.userToBeEdited.lower():
                    self.logger.info(self.userToBeEdited + "User found and the started editing the user")
                    # userEditErrorDisplay = self.driver.find_element(By.XPATH, self.userEditError)

                    xPath = self.editUserDynamicXpath.format(i + 2)
                    self.driver.find_element(By.XPATH, xPath).click()
                    time.sleep(5)

                    if not self.getStaleElement(self.userEditError):
                        #time.sleep(5)
                        #self.driver.find_element(By.XPATH,self.editUserNameXPath).clear()
                        self.driver.find_element(By.XPATH, self.editUserNameXPath).send_keys(userName)
                        #self.driver.find_element(By.XPATH,self.editAccessKeyXPath).clear()
                        self.driver.find_element(By.XPATH, self.editAccessKeyXPath).send_keys(accessKey)
                        #self.driver.find_element(By.XPATH,self.editFullNameXPath).clear()
                        self.driver.find_element(By.XPATH, self.editFullNameXPath).send_keys(fullName)
                        #self.driver.find_element(By.XPATH,self.editEmailXPath).clear()
                        self.driver.find_element(By.XPATH, self.editEmailXPath).send_keys(emailId)
                        self.driver.find_element(By.XPATH,self.updateUserXpath).click()
                        return True
                    else:
                        self.logger.info("Deactivate the license first")
                        return False
            return False
        except Exception as e:
            self.logger.info("Exception occurred in validating the edit user page")
            self.logger.info(e)
            return False


    def validate_delete_user_page(self):
        try:
            self.logger.info("deleting the user started")
            self.driver.get(self.usersUrl)
            self.logger.info("Navigated to the users URL page")
            userList = self.driver.find_elements(By.XPATH, '//*[@id="ctl00_mainContent_gvUsers"]/tbody/tr/td[2]')
            for i in userList:
                if i.text.lower() == self.userToBeDeleted.lower():
                    self.logger.info("User found to delete")
                    print(userList.index(i))
                    indexVal = userList.index(i)
                    xPath = '//*[@id="ctl00_mainContent_gvUsers"]/tbody/tr/td[9]/input'
                    self.driver.find_element(By.XPATH, xPath).click()
                    self.driver.switch_to.alert.accept()
                    time.sleep(5)
                    return True
            else:
                self.logger.info("User Not Found for delete")
                return False

        except Exception as e:
            self.logger.info("Exception occurred in deleting the user page")
            return False