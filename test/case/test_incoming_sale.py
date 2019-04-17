# _*_ coding:utf-8 _*_

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL="http://192.168.3.181:9155"
base_path = os.path.dirname(os.path.abspath(__file__)) + '\..\..'
driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')

#print(driver_path)
locator_company = (By.ID, "applyCompanyName")
locator_status = (By.ID, "status")
locator_status_value = (By.CSS_SELECTOR, "li.ant-select-dropdown-menu-item.ant-select-dropdown-menu-item-active")
locator_date = (By.ID, "rangePicker")
locator_query = (By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
locator_companyName = (By.XPATH,"//td[@class='ant-table-column-has-actions ant-table-column-has-sorters']/../td[2]")
locator_enter = (By.XPATH,"//tbody[@class='ant-table-tbody']/tr[1]/td[6]/div/a")
locator_enter_sale = (By.XPATH,"//td[@class='ant-table-column-has-actions ant-table-column-has-sorters' and contains(text(),'委托销售')]/../td[6]/div/a")

driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
try:
    driver.get(URL)
    driver.find_element(*locator_company).send_keys('白杨')
    driver.find_element(*locator_status).click()
    driver.implicitly_wait(1)
    driver.find_element(*locator_status_value).click()
    driver.find_element(*locator_query).click()
    driver.implicitly_wait(3)
    #driver.find_elements(*locator_enter_sale)[0].click()
    companyNames = driver.find_elements(*locator_companyName)
    for companyName in companyNames:
        print(companyName.text)


except Exception as e :
    print(e)
    print(driver.page_source)

finally:
    time.sleep(3)
    driver.quit()