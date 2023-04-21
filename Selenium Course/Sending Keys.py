from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
driver.implicitly_wait(5)
try:
    no_button = driver.find_element("class", "at-cm-no-button")
    no_button.click()
except:
    print("No element")

sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(by='sum2')
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)
sum2.send_keys(15)
btn = driver.find_element(By.CSS_SELECTOR, "button[onclick='return total()']")
