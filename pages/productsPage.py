import time
from selenium.webdriver.common.by import By




class ProductPage:
    productUrl = 'https://staging.epiplex500.com/Reports/Rpt_ProductDetails.aspx'
    exportExcelXPath = '//*[@id="ctl00_mainContent_ImgExport"]'
    def __init__(self,driver,logger):
        self.driver = driver
        self.logger = logger

    def navigate_to_url(self):
        try:
            self.logger.info("Navigate to Product Page URL started")
            self.driver.get(self.productUrl)
            self.logger.info("Navigate to Product Page URL Ended")
        except Exception as e:
            self.logger.info("Exception occured in navigating the URL")
            self.logger.info(e)
            return False
    def validate_product_page(self):
        try:
            self.logger.info("Validating the product page started")
            self.driver.find_element(By.XPATH,self.exportExcelXPath).click()
            time.sleep(2)
            return True
        except Exception as e:
            self.logger.info("Exception occured in validating the Product Page")
            self.logger.info(e)
            return False

