from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ser = Service(r"C:\chromedriver.exe")
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)
s.get("http://google.com/")
print("Headless Chrome Initialized")