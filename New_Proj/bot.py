import os
import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from New_Proj.open_url import OpenUrl


# class Table(webdriver.Chrome):
#     def __init__(self, driver_path=r"C:\Development\chromedriver.exe", teardown=False):
#         ser = Service(r"C:\Development\chromedriver.exe")
#         option = webdriver.ChromeOptions()
#         self.driver_path = driver_path
#         super(Table, self).__init__(service=ser, options=option)
#         self.teardown = teardown
#         os.environ['PATH'] += self.driver_path
#         self.implicitly_wait(15)
class Bot(OpenUrl):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome()

    def results(self, navigate_to_urls1, url_list):
        self.navigate_to_urls1(url_list)
        price_min = self.driver.find_element(By.ID, "minPrice_")
        price_min.click()
