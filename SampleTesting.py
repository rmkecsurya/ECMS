

















# import time
# import openpyxl
# from xlwt import Workbook
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from openpyxl import Workbook
# from pages.loginPage import LoginPage
# from selenium import webdriver
#
#
# def htmlToXsl(sheetneme, headerowXpath, headercolumnXpath, HeaderCellsXpath, datacellsXpath, xlsFilepath):
#     r = driver.find_elements(By.XPATH, headerowXpath)
#     c = driver.find_elements(By.XPATH, headercolumnXpath)
#     wb = Workbook()
#     sheet = wb.add_sheet(sheetneme)
#     for i in range(1, len(r) + 1):
#         for j in range(1, len(c) + 1):
#             if i == 1:
#                 d = driver.find_element(By.XPATH, HeaderCellsXpath).text
#
#                 sheet.write(i, j, d)
#             else:
#                 d = driver.find_element(By.XPATH, datacellsXpath).text
#                 sheet.write(i, j, d)
#     wb.save(xlsFilepath)
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get('https://staging.epiplex500.com/')
# driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_txtUserName"]').send_keys('mandanna')
# driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_txtPassword"]').send_keys('password123')
# driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_LoginButton"]').click()
#
#
# #Add new User Page
# # driver.get('https://staging.epiplex500.com/Users/CreateUser.aspx')
# # driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_txtUsername"]').send_keys("Surya")
# # driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_txtAccesskey"]').send_keys("Surya@123")
# # driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_txtName"]').send_keys("surya.n")
# # driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_txtEmail"]').send_keys("surya.n@epiance.com")
# # driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_ddlGroupName"]').send_keys("kumar")
# # driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_chkPublicUser"]').click()
# # driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_btnCreateUser"]').click()
# # time.sleep(10)
#
# #License Allocation
#
#
# # driver.get('https://staging.epiplex500.com/ManageLicense/Licenses.aspx')
# # driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_gvLicenses"]/tbody/tr[2]/td[1]/a').click()
# # time.sleep(3)
# # driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_gvLicenses_ctl02_GridView2_ctl02_btnRelease"]').click()
# # print(driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_gvRelease"]/tbody/tr/td').is_displayed())
#
#
# driver.get('https://staging.epiplex500.com/Reports/Rpt_History.aspx')
# # web = driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_ImgPrint"]')
# # web.click()
# # web.send_keys(Keys.TAB)
# # web.send_keys(Keys.ENTER)
# driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_DropDownGroupNames"]').send_keys('---Select a Group---')
# print(driver.find_element(By.XPATH,'//*[@id="ctl00_mainContent_GridView1"]/tbody/tr/td').text)
# # driver.send_keys()
#
#
#
#
