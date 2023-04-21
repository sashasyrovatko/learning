from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
class ResultReport(webdriver.Chrome):
    def __init__(self):
        super().__init__()

