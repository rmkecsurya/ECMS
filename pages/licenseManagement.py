import time
from selenium.webdriver.common.by import By
from configuration.config import Config as config


class LicenceManagement:
    licensePageUrl = 'https://staging.epiplex500.com/ManageLicense/Licenses.aspx'
    userXpath = '//*[@id="ctl00_mainContent_gvLicenses"]/tbody/tr/td[2]'
    allocateGrpXPath = '//*[@id="ctl00_mainContent_ddlGroups"]/option'
    productGrpXPath = '//*[@id="ctl00_mainContent_ddlProducts"]/option'
    allocateComboXPath = '//*[@id="ctl00_mainContent_ddlAvailableLic"]/option'
    allocateBtnXPath = '//*[@id="ctl00_mainContent_btnAllocate"]'
    licenseNotAvailableError = '//*[@id="ctl00_mainContent_tableMessage"]/tbody/tr/td'
    releasingLicenseNoRecordFoundXpath = '//*[@id="ctl00_mainContent_gvRelease"]/tbody/tr/td'
    allocateLicenseDynamicXpath = '//*[@id="ctl00_mainContent_gvLicenses"]/tbody/tr[{0}]/td/div/div/table/tbody/tr[2]/td[4]/input'
    releaseLicenseDynamicXPath = '//*[@id="ctl00_mainContent_gvLicenses"]/tbody/tr[{0}]/td/div/div/table/tbody/tr[2]/td[5]/input'
    licenseCountDynamicXpath1 = '//*[@id="ctl00_mainContent_ddlAvailableLic"]/option[{0}]'
    licenseCountDynamicXpath2 = '//*[@id="ctl00_mainContent_ddlAvailableLic"]/option[1]'
    releaseSearchTxtBoxXpath = '//*[@id="ctl00_mainContent_txtSearch"]'
    releaseSearchBtnXpath = '//*[@id="ctl00_mainContent_btnSearch"]'
    releaseTableXPath = '//*[@id="ctl00_mainContent_gvRelease"]/tbody/tr/td[3]'
    userGrpToBeRelease = 'NMuser'
    releaseBtnXPath = '//*[@id="ctl00_mainContent_btnReleaseLic_top"]'
    releaseLicenseToUserXPath = '//*[@id="ctl00_mainContent_gvRelease"]/tbody/tr/td/span/input'

    releaseToUser = config.releaseToUser
    allocateToUser = config.allocateToUser
    grpUserName = config.grpUserName
    productName = config.productName

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def checkElementExists(self, xPath):
        try:
            self.driver.find_element(By.XPATH, xPath)
            return True
        except:
            return False

    def navigate_to_url(self):
        try:
            self.logger.info("Navigating to the License Management URL")
            self.driver.get(self.licensePageUrl)
        except Exception as e:
            self.logger.info("Exception occurred in Navigating to the URL")
            self.logger.info(e)
            return False

    def validate_allocate_license_to_user(self):
        try:
            self.logger.info("Validating the Allocate License to user page started")
            j = 2
            users = self.driver.find_elements(By.XPATH, self.userXpath)
            for i in range(0, len(users), 2):
                print(users[i].text)
                if users[i].text == self.allocateToUser:
                    xpath = '//*[@id="ctl00_mainContent_gvLicenses"]/tbody/tr[{0}]/td[1]/a'.format(j)
                    self.driver.find_element(By.XPATH, xpath).click()
                    licenseXpath = self.allocateLicenseDynamicXpath.format(j + 1)
                    self.driver.find_element(By.XPATH, licenseXpath).click()
                    # self.driver.find_element(By.XPATH,self.licenseNotAvailableError).is_displayed():
                    if not self.checkElementExists(self.licenseNotAvailableError):
                        availableLicenseCount = self.driver.find_elements(By.XPATH, self.allocateComboXPath)
                        if len(availableLicenseCount) > 2:
                            for i in range(len(availableLicenseCount) // 2, 0, -1):
                                licenseCountXPath = self.licenseCountDynamicXpath1.format(i)
                                self.driver.find_element(By.XPATH, licenseCountXPath).click()
                                self.driver.find_element(By.XPATH, self.allocateBtnXPath).click()
                                return True
                        elif len(availableLicenseCount) < 2 and len(availableLicenseCount) > 0:
                            licenseCountXPath = self.licenseCountDynamicXpath2
                            self.driver.find_element(By.XPATH, licenseCountXPath).click()
                            self.driver.find_element(By.XPATH, self.allocateBtnXPath).click()
                            break
                    else:
                        self.logger.info("License not available for the user")
                        return False
                j += 2
            return True
        except Exception as e:
            self.logger.info("Exception occurred in the allocating license to user page")
            self.logger.info(e)
            return False

    def validate_release_license_to_user(self):
        try:
            self.logger.info("Validating the Release License To User Started")
            j = 2
            users = self.driver.find_elements(By.XPATH, self.userXpath)
            for i in range(0, len(users), 2):
                print(users[i].text)
                if users[i].text == self.releaseToUser:
                    xpath = '//*[@id="ctl00_mainContent_gvLicenses"]/tbody/tr[{0}]/td[1]/a'.format(j)
                    self.driver.find_element(By.XPATH, xpath).click()
                    licenseXpath = self.releaseLicenseDynamicXPath.format(j + 1)
                    self.driver.find_element(By.XPATH, licenseXpath).click()
                    if not self.driver.find_element(By.XPATH, self.releasingLicenseNoRecordFoundXpath).is_displayed():
                        self.logger.info("Validating the Release License To User Failed Due to No Records Found Error")
                        return False
                    else:
                        checkBoxList = self.driver.find_elements(By.XPATH,self.releaseLicenseToUserXPath)
                        for i in range(len(checkBoxList)//2):
                            xpath = '//*[@id="ctl00_mainContent_gvRelease"]/tbody/tr[{0}]/td/span/input'.format(i+2)
                            self.driver.find_element(By.XPATH,xpath).click()
                        self.logger.info("Validating the Release License To User successful")
                        return True
                j += 2
        except Exception as e:
            self.logger.info("Exception raised in the Validating the license")
            self.logger.info(e)
            return False

    def validate_allocateLicense(self):
        try:
            self.driver.get('https://staging.epiplex500.com/ManageLicense/AllocateLic.aspx')
            users = self.driver.find_elements(By.XPATH, self.allocateGrpXPath)
            for i in range(1, len(users)):
                # print(users[i].text)
                if users[i].text.lower() == self.grpUserName.lower():
                    xpath = ('//*[@id="ctl00_mainContent_ddlGroups"]/option[{0}]').format(i + 1)
                    self.driver.find_element(By.XPATH, xpath).click()
                    break
            products = self.driver.find_elements(By.XPATH, self.productGrpXPath)
            for i in range(1, len(products)):
                if products[i].text == self.productName:
                    xpath = ('//*[@id="ctl00_mainContent_ddlProducts"]/option[{0}]').format(i + 1)
                    self.driver.find_element(By.XPATH, xpath).click()
                    break
            return True
        except Exception as e:
            self.logger.info("Exception occured in Allocation Page")
            self.logger.info(e)
            return False

    def validate_releaseLicense(self):
        try:
            self.driver.get("https://staging.epiplex500.com/ManageLicense/ReleaseLic.aspx")
            self.driver.find_element(By.XPATH, self.releaseSearchTxtBoxXpath).send_keys(self.userGrpToBeRelease)
            self.driver.find_element(By.XPATH, self.releaseSearchBtnXpath).click()
            if self.driver.find_element(By.XPATH, self.releasingLicenseNoRecordFoundXpath).text == 'No Record Found':
                return False
            else:
                groups = self.driver.find_elements(By.XPATH, self.releaseTableXPath)
                for i in range(2, 7):
                    if groups[i].text.lower() == self.userGrpToBeRelease.lower():
                        xPath = '//*[@id="ctl00_mainContent_gvRelease"]/tbody/tr[{0}]/td[1]/span/input'.format(i)
                        self.driver.find_element(By.XPATH, xPath).click()
                self.driver.find_element(By.XPATH, self.releaseBtnXPath)
                return True
        except Exception as e:
            self.logger.info("Exception occurred in release License Page")
            self.logger.info(e)
            return False
