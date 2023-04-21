import os
import pandas
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from main import ReadCsv

class Table(webdriver.Chrome):
    def __init__(self, driver_path="C:\Development\chromedriver.exe", teardown=False):
        ser = Service(r"C:\Development\chromedriver.exe")
        option = webdriver.ChromeOptions()
        super().__init__(service=ser, options=option)
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        self.implicitly_wait(15)



