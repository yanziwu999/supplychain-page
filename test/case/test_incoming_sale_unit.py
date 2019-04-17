# _*_ coding:utf-8 _*_

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH

class TestSaleInput(unittest.TestCase):
    URL = Config().get('URL')

    locator_company = (By.ID, "applyCompanyName")
    locator_status = (By.ID, "status")
    locator_status_value = (By.CSS_SELECTOR, "li.ant-select-dropdown-menu-item.ant-select-dropdown-menu-item-active")
    locator_date = (By.ID, "rangePicker")
    locator_query = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
    locator_companyName = (By.XPATH, "//td[@class='ant-table-column-has-actions ant-table-column-has-sorters']/../td[2]")
    locator_enter = (By.XPATH, "//tbody[@class='ant-table-tbody']/tr[1]/td[6]/div/a")
    locator_enter_sale = (By.XPATH, "//td[@class='ant-table-column-has-actions ant-table-column-has-sorters' and contains(text(),'委托销售')]/../td[6]/div/a")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(self.URL)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()


    def test_search_sale(self):
        self.driver.find_element(*self.locator_company).send_keys('白杨')
        self.driver.find_element(*self.locator_status).click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(*self.locator_status_value).click()
        self.driver.find_element(*self.locator_query).click()
        self.driver.implicitly_wait(3)
        self.driver.find_elements(*self.locator_enter_sale)[0].click()

    def test_search(self):
        self.driver.find_element(*self.locator_company).send_keys('白杨')
        self.driver.find_element(*self.locator_status).click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(*self.locator_status_value).click()
        self.driver.find_element(*self.locator_query).click()
        self.driver.implicitly_wait(3)
        companyNames = self.driver.find_elements(*self.locator_companyName)
        for companyName in companyNames:
            print(companyName.text)

if __name__ == '__main__':
    unittest.main()
