from selenium import webdriver
from configuration.config import Config
from pages.activationHistoryPage import ActivationHistory
from pages.activationReportPage import ActivatePage
from pages.allocationPage import AllocationReportPage
from pages.changePasswordPage import ChangePasswordPage
from pages.checkoutHistoryPage import CheckOutHistoryPage
from pages.checkoutStatusPage import CheckoutStatusPage
from pages.failedRequestPage import FailedRequestPage
from pages.forceDeactivatePage import ForceDeactivatingPage
from pages.groupPage import GroupPage
from pages.licenseManagement import LicenceManagement
from pages.licenseUtilizationPage import LicenseUtilizationPage
from pages.loginPage import LoginPage
from pages.myProfilePage import MyProfilePage
from pages.productsPage import ProductPage
from pages.recoverUsersPage import RecoverUserPage
from pages.signOutPage import SignOutPage
from pages.userPage import UserPage
from utilities.customLogger import LogGen

# Chrome driver initialization
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
logger = LogGen.loggen()
config = Config()


def test_validate_loginPage():
    logger.info("*******Test Login Page Testcase Started*******")
    loginPage = LoginPage(driver, config.username, config.password, logger)
    loginPage.navigate_to_url()
    loginPage.validate_login()
    assert driver.title == 'Home- Epiplex License Management System'

    if driver.title == 'Home- Epiplex License Management System':
        logger.info("SuccessFully Signed In")
        assert True
    else:
        # print("Login is not successful")
        logger.info("Failed to  Signed In")
        assert False

    logger.info("*******Test LoginPage Ended*******")

#error in importing
def test_validate_add_new_user():
    logger.info("*******Add New User TestCase Started*******")
    userPageObj = UserPage(driver, logger)
    result = userPageObj.validate_add_new_user()
    if result:
        logger.info("Add new User Testcase Passed")
        assert True
    else:
        logger.info("Add new User Testcase Failed")
        assert False
    logger.info("*******Add New User TestCase Ended*******")

def test_validate_search_user():
    logger.info("*******Searching for the user TestCase Started*******")
    userPageObj = UserPage(driver, logger)
    result = userPageObj.validate_search_user()
    if result:
        logger.info("Search Testcase Passed")
        assert True
    else:
        logger.info("Search Testcase Failed")
        assert False

    logger.info("*******Searching for the user TestCase Ended*******")

def test_validate_edit_user_page():
    logger.info("*******Editing user TestCase Started*******")
    userPageObj = UserPage(driver, logger)
    result = userPageObj.validate_edit_user_page()
    if result:
        assert True
    else:
        assert False
    logger.info("*******Editing user TestCase Ended*******")


def test_validate_delete_user():
    logger.info("*******Deleting user TestCase Started*******")
    userPageObj = UserPage(driver,logger)
    result = userPageObj.validate_delete_user_page()
    if result:
        assert True
    else:
        assert False
    logger.info("*******Deleting user TestCase Ended*******")

def test_validate_add_new_group():
    logger.info("*******Adding new group TestCase Started*******")
    grpPageObj = GroupPage(driver,logger)
    result = grpPageObj.validate_add_new_groupPage()
    if result:
        logger.info("Adding new Group TestCase Passed")
        assert True
    else:
        logger.info("Adding new Group TestCase Failed")
        assert False
    logger.info("*******Adding new group TestCase Ended*******")

def test_validate_edit_groupPage():
    logger.info("*******Editing the group TestCase Started*******")
    grpPageObj = GroupPage(driver,logger)
    grpPageObj.navigate_toURL()
    grpEditResult = grpPageObj.validate_edit_groupPage()
    if grpEditResult:
        logger.info("Editing the group TestCase Passed")
        assert True
    else:
        logger.info("Editing the group TestCase Failed")
        assert False
    logger.info("*******Editing the group TestCase Ended*******")
def test_validate_delete_groupPage():
    grpPageObj = GroupPage(driver,logger)
    grpPageObj.navigate_toURL()
    deleteGrpResult = grpPageObj.validate_delete_group()
    if deleteGrpResult:
        assert True
    else:
        assert False
def test_validate_search_groupPage():
    grpPageObj = GroupPage(driver,logger)
    grpPageObj.navigate_toURL()
    searchGrpResult = grpPageObj.validate_search_group()
    if searchGrpResult:
        assert True
    else:
        assert False

def test_validate_search_recoverUser():
    recoverUserObj = RecoverUserPage(driver,logger)
    recoverUserObj.navigate_to_url()
    searchRecoverUser = recoverUserObj.validate_recovery_search()
    if searchRecoverUser:
        assert True
    else:
        assert False
def test_validate_recoverUser():
    recoverUserObj = RecoverUserPage(driver,logger)
    recoverUserObj.navigate_to_url()
    searchRecoverUser = recoverUserObj.validate_recovery_page()
    if searchRecoverUser:
        assert True
    else:
        assert False


def test_validate_allocate_license_to_user():
    licenseManagementObj = LicenceManagement(driver,logger)
    licenseManagementObj.navigate_to_url()
    result = licenseManagementObj.validate_allocate_license_to_user()
    if result:
        assert True
    else:
        assert False
    # groupToBeAllocated = 'Test'
    # productToBeAllocated = 'Epiplex500 Desktop Capture - 7.7 [24/02/2015]'
    # licenseManagementObj.allocateLicense(groupToBeAllocated, productToBeAllocated)
def test_validate_release_license_to_user():
    licenseManagementObj = LicenceManagement(driver,logger)
    licenseManagementObj.navigate_to_url()
    result = licenseManagementObj.validate_release_license_to_user()
    if result:
        assert True
    else:
        assert False

def test_validate_allocate_license():
    licenseManagementObj = LicenceManagement(driver, logger)
    #licenseManagementObj.allocateLicense()
    result = licenseManagementObj.validate_allocateLicense()
    if result:
        assert True
    else:
        assert False

def test_validate_release_license():
    licenseManagementObj = LicenceManagement(driver, logger)
    #licenseManagementObj.allocateLicense()
    result = licenseManagementObj.validate_releaseLicense()
    if result:
        assert True
    else:
        assert False


def test_validate_products_report():
    logger.info("*******Products TestCase Started*******")
    productPageObj = ProductPage(driver,logger)
    productPageObj.navigate_to_url()
    resut = productPageObj.validate_product_page()
    if resut:
        assert True
    else:
        assert False
    logger.info("*******Products TestCase Ended*******")

def test_validate_activation_report():
    activateObj = ActivatePage(driver,logger)
    activateObj.navigate_to_URL()
    result = activateObj.validate_activation_report_page()
    if result:
        assert True
    else:
        assert False

def test_validate_allocation_report():
    logger.info("*******Allocation Report TestCase Started*******")
    allocationPageObj = AllocationReportPage(driver,logger)
    allocationPageObj.navigate_to_url()
    result = allocationPageObj.validate_allocation_page()
    if result:
        assert True
    else:
        assert False
    logger.info("*******Allocation Report TestCase Ended*******")

def test_validate_activation_history():
    logger.info("*******Activation History Page TestCase started*******")
    activationHistoryPageObj = ActivationHistory(driver,logger)
    activationHistoryPageObj.navigate_to_url()
    result = activationHistoryPageObj.validate_activation_history_page()
    if result:
        logger.info("Activation History TestCase Passed*******")
        assert True
    else:
        logger.info("Activation History TestCase Failed*******")
        assert False
    logger.info("*******Activation History Page TestCase Ended*******")

def test_validate_checkout_status():
    logger.info("*******Checkout status Page TestCase started*******")
    checkoutStatusPageObj = CheckoutStatusPage(driver,logger)
    checkoutStatusPageObj.navigate_to_url()
    result = checkoutStatusPageObj.validate_checkout_status_page()
    if result:
        assert True
    else:
        assert False
    logger.info("*******Checkout status Page TestCase Ended*******")

def test_validate_checkout_history():
    logger.info("*******Checkout history Page TestCase started*******")
    checkOutHistoryPageObj = CheckOutHistoryPage(driver,logger)
    checkOutHistoryPageObj.navigate_to_url()
    result = checkOutHistoryPageObj.validate_checkout_history_page()
    if result:
        assert True
    else:
        assert False
    logger.info("*******Checkout history Page TestCase Ended*******")

def test_validate_failed_request_page():
    logger.info("*******Validating the Failed Request Page Testcase Started*******")
    checkOutHistoryPageObj = FailedRequestPage(driver, logger)
    checkOutHistoryPageObj.naviagte_to_url()
    result = checkOutHistoryPageObj.validate_failed_request_page()
    if result:
        assert True
    else:
        assert False
    logger.info("*******Validating the Failed Request Page Testcase Ended*******")

def test_validate_force_deactivation_page():
    logger.info("*******Validating the Failed Request Page Testcase Started*******")
    forceDeactivationPageOBJ = ForceDeactivatingPage(driver, logger)
    forceDeactivationPageOBJ.navigate_to_url()
    result = forceDeactivationPageOBJ.validate_force_deactivation_page()
    if result:
        assert True
    else:
        assert False
    logger.info("*******Validating the Failed Request Page Testcase Ended*******")

def test_validate_failed_activation_page():
    logger.info("*******Validating the Failed activation Page Testcase Started*******")
    forceDeactivationPageOBJ = ForceDeactivatingPage(driver, logger)
    forceDeactivationPageOBJ.navigate_to_url()
    result = forceDeactivationPageOBJ.validate_force_deactivation_page()
    if result:
        assert True
    else:
        assert False
    logger.info("*******Validating the Failed activation Page Testcase Ended*******")

def test_validate_license_utilization_page():
    logger.info("*******Validating the Failed activation Page Testcase Started*******")
    licenseUtilicationPageObj = LicenseUtilizationPage(driver, logger)
    licenseUtilicationPageObj.navigate_to_url()
    result = licenseUtilicationPageObj.validate_license_utilization_page()
    if result:
        assert True
    else:
        assert False
    logger.info("*******Validating the Failed activation Page Testcase Ended*******")

def test_validate_myprofile_page():
    logger.info("*******Validating the MyProfile Testcase Started*******")
    myProfilePageObj = MyProfilePage(driver, logger)
    myProfilePageObj.navigate_to_url()
    result = myProfilePageObj.validate_myprofile_page()
    if result:
        assert True
    else:
        assert False
    logger.info("*******Validating the MyProfile Testcase Ended*******")

def test_validate_myprofile_page():
    logger.info("*******Validating the Change Password Testcase Started*******")
    changePasswordPageObj = ChangePasswordPage(driver, logger)
    changePasswordPageObj.navigate_to_url()
    result = changePasswordPageObj.validate_change_password_page()
    if result:
        assert True
    else:
        assert False
    logger.info("*******Validating the Change Password Testcase Ended*******")

def test_validate_sign_out():
    logger.info("*******Signout Page TestCase Started*******")
    signOutPageObj = SignOutPage(driver,logger)
    signOutPageObj.Validate_signOut_page()
    logger.info("*******Signout Page TestCase Ended*******")

