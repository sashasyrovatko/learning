from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from BrainProj.brain.brain_filtrations import BrainFiltration
from BrainProj.brain.brain_report import BrainReport
from prettytable import PrettyTable

chrom_driver_path = "C:\Development\chromedriver.exe"
class Brain(webdriver.Chrome):
    def __init__(self, driver_path=chrom_driver_path, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        ser = Service(r"C:\Development\chromedriver.exe")
        option = webdriver.ChromeOptions()
        super(Brain, self).__init__(options=option, service=ser)
        self.implicitly_wait(15)

    def search_page(self):
        self.get("https://brain.com.ua/ukr/")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def city_choice(self, city):
        city_element = self.find_element(By.CSS_SELECTOR,
                                         'button[class="mycity_container mycity mycityname"]')
        city_element.click()
        enter_city = self.find_element(By.CSS_SELECTOR,
                                       "input[placeholder='Почніть вводити назву']")
        enter_city.clear()
        enter_city.send_keys(city)
        results = self.find_element(By.CSS_SELECTOR,
                                    'div[tabindex="0"]')
        results.click()

    def search_element(self, name_search):
        search_field = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/header/div[2]/div/div/div[2]/form/input[1]'))
        )
        search_field.click()
        search_field.clear()
        search_field.send_keys(name_search)
        search_field.send_keys(Keys.ENTER)

    def categories(self, price_from, price_to):
        filtration = BrainFiltration(driver=self)
        filtration.apply_filtration()
        cost_from = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]'
                                        '/div/div[2]/div/div[2]/div[2]/div[2]/input[1]')))
        cost_from.click()
        cost_from.send_keys(price_from)
        cost_to = self.find_element(By.XPATH,
                                    '/html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]'
                                    '/div/div[2]/div/div[2]/div[2]/div[2]/input[2]')
        cost_to.click()
        cost_to.send_keys(price_to)
        find = self.find_element(By.XPATH,
                                 '/html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]'
                                 '/div/div[2]/div/div[2]/div[2]/div[2]/a')
        find.click()

    def report_results(self):
        results_list = self.find_element(By.CSS_SELECTOR,
                                         'div[class="view-grid tab-pane row br-row br-flex active"]'
                                         )

        report = BrainReport(results_list)
        table = PrettyTable(
            field_names=["Name", "Price", "Score"]
        )
        table.add_rows(report.pull_titles())
        print(table)
