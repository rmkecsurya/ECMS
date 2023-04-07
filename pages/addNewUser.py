import time

from selenium.webdriver.common.by import By


class AddNewUser:
    userNameXPath = '//*[@id="ctl00_mainContent_txtUsername"]'
    accessKeyXPath = '//*[@id="ctl00_mainContent_txtAccesskey"]'
    # this should be user defined not the static type
    fullNameXpath = '//*[@id="ctl00_mainContent_txtName"]'
    emailXpath = '//*[@id="ctl00_mainContent_txtEmail"]'
    gropNameXPath = '//*[@id="ctl00_mainContent_ddlGroupName"]/option'
    publicUserCheckBoxXpath = '//*[@id="ctl00_mainContent_chkPublicUser"]'
    managerXPath = '//*[@id="ctl00_mainContent_chkIsManager"]'
    createUserBtnXPath = '//*[@id="ctl00_mainContent_btnCreateUser"]'
    cancelUserCreationBtnXPath = '//*[@id="ctl00_mainContent_btnCancel"]'
    errorDisplayXPath = '//*[@id="ctl00_mainContent_ValidationSummary1"]'

    def __init__(self, driver, url,logger):
        self.driver = driver
        self.url = url
        self.logger = logger
        # self.addNewUserXPath = addNewUserXPath

    def navigate_toURL(self):
        # pass
        try:
            self.driver.get(self.url)
            self.logger.info("Successfully navigated to the Add new user page page")
        except:
            self.logger.info("Exception occured in the Navigating to the user creation page")
            return False

    def newUserCreateion(self, userName, accessKey, fullName, emailId):
        # self.driver.find_element(By.XPATH, self.m6).click()
        try:
            self.logger.info("Adding New User Creation Started")
            if self.driver.title == "Create new user- Epiplex License Management System":
                self.logger.info("Successfully logged into add new user page")
                #Sending the username for creation of user
                self.driver.find_element(By.XPATH, self.userNameXPath).send_keys(userName)
                # Sending the accesskey for creation of user
                self.driver.find_element(By.XPATH, self.accessKeyXPath).send_keys(accessKey)
                # Sending the fullname for creation of user
                self.driver.find_element(By.XPATH, self.fullNameXpath).send_keys(fullName)
                # Sending the email id for creation of user
                self.driver.find_element(By.XPATH, self.emailXpath).send_keys(emailId)
                grpNameList = self.driver.find_elements(By.XPATH, self.gropNameXPath)
                grpNameList[2].click()
                self.driver.find_element(By.XPATH, self.publicUserCheckBoxXpath).click()
                # time.sleep(6)
                self.driver.find_element(By.XPATH, self.managerXPath).click()
                self.driver.find_element(By.XPATH, self.createUserBtnXPath).click()
                errorDisplay = self.driver.find_element(By.XPATH, self.errorDisplayXPath)
                if errorDisplay.is_displayed():
                    self.logger.info("Entered Display is not correct")
                    return False
                else:
                    #print("Details Entered are correct")
                    self.logger.info("Entered Display correct")
                    return True
                # self.driver.find_element(By.XPATH,self.createUserBtnXPath).click()
                # if option == 1:
                #     print("Create User")
                #     self.driver.find_element(By.XPATH,self.createUserBtnXPath).click()
                #     errorDisplay = self.driver.find_element(By.XPATH,self.errorDisplayXPath)
                #     time.sleep(6)
                #     if errorDisplay.is_displayed():
                #         print("Entered display is not correct")
                #     else:
                #         print("Details Entered are correct")
                #
                # else:
                #     print("Abort the user creation")
                #     self.driver.find_element(By.XPATH, self.cancelUserCreationBtnXPath).click()
                # #The user group should be selected by the user not to hard code it.
                # for i in grpNameList:
                #     pass
            else:
                self.logger.info("Landed in the Invalid User Page")
                return False
        except Exception as e:
            self.logger.info("Exception occured in the new user creation page")
            self.logger.info(e)
            return False
