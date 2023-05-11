import re
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from New_Proj.reader import ReaderCsv
import pandas



class OpenUrl(ReaderCsv):
    def __init__(self):
        super().__init__("file.csv")
        self.driver = webdriver.Chrome()
        self.data_writer = ReaderCsv('file.csv')

    # '0,https://m.ua/m1_magazilla.php?katalog_=206,10000,20000'
    # https://m.ua/ua/m1_magazilla.php?katalog_=206&order_=pop&save_podbor_=1&minPrice_=10000&maxPrice_=20000&sc_id_=980
    # def navigate_to_urls1(self):
    #     model_list = []
    #     self.driver.get('https://m.ua/ua/m1_magazilla.php?katalog_=206&minPrice_=10000&maxPrice_=20000')
    #     pages_element = self.driver.find_element(By.XPATH, "//*[@id='list']/tbody/tr[17]/td/div/div/span")
    #     pages_text = pages_element.text
    #     pages_num = int(pages_text.split()[-1])
    #     for page in range(1, pages_num + 1):
    #         models = self.driver.find_elements(By.CLASS_NAME, "list-model-title")
    #         prices = self.driver.find_elements(By.XPATH, "//a[@title='Порівняти ціни! ']")
    #         for i in range(len(models)):
    #             model_name = models[i].text
    #             price = prices[1].text
    #             model_list.append((model_name, price))
    #         if page != pages_num:
    #             next_page_button = self.driver.find_element(By.CSS_SELECTOR, "a[id='pager_next']")
    #             next_page_button.click()
    #             WebDriverWait(self.driver, 10).until(
    #                 EC.presence_of_element_located((By.CLASS_NAME, "list-model-title")))
    #     print(pages_num)
    #     print(model_list)

    def navigate_to_urls1(self):
        model_dict = {}
        # urls = self.get_url_list()
        #
        # for url in urls:
        #     self.driver.get(url)

        self.driver.get('https://m.ua/ua/m1_magazilla.php?katalog_=206&minPrice_=10000&maxPrice_=20000')

        while True:
                models = self.driver.find_elements(By.CLASS_NAME, "list-model-title")
                prices = self.driver.find_elements(By.XPATH, "//a[@title='Порівняти ціни! ']")

                for i in range(min(len(models), len(prices))):
                    model_name = models[i].text
                    price = prices[i].text
                    price = re.sub(r'\D', '', price)
                    model_dict[model_name] = price

                try:
                    next_page_button = self.driver.find_element(By.CSS_SELECTOR, "a[id='pager_next']")
                    self.driver.execute_script("arguments[0].click();", next_page_button)
                    time.sleep(1)
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "list-model-title")))
                except NoSuchElementException:
                    break
        return model_dict



    def navigate_to_all_pages(self):
        model_list = []
        self.driver.get('https://m.ua/ua/m1_magazilla.php?katalog_=206&minPrice_=10000&maxPrice_=20000')

        models_per_page = len(self.driver.find_elements(By.CLASS_NAME, "list-model-title"))
        selected_models = int(
            self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Вибрано')]")[0].text.split()[1])

        total_pages = (selected_models + models_per_page - 1) // models_per_page

        for page in range(1, total_pages + 1):
            models = self.driver.find_elements(By.CLASS_NAME, "list-model-title")
            prices = self.driver.find_elements(By.XPATH, "//a[@title='Порівняти ціни! ']")

            for i in range(min(len(models), len(prices))):
                model_name = models[i].text
                price = prices[i].text
                model_list.append((model_name, price))

            if page != total_pages:
                next_page_button = self.driver.find_element(By.CSS_SELECTOR, "a[id='pager_next']")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", next_page_button)
                next_page_button.click()
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "list-model-title")))

        for model in model_list:
            print(f"Model: {model[0]}, Price: {model[1]}")


        # num_text = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Вибрано')]").text
        # num = int(num_text.split()[-2])
        # print(num)

        # self.driver.get('https://m.ua/ua/m1_magazilla.php?katalog_=206&minPrice_=10000&maxPrice_=20000')
        # price_min = self.find_element(By.ID, "minPrice_")
        # price_min.click()
        # price_min.send_keys("10000")
        # price_max = self.find_element(By.ID, "maxPrice_")
        # price_max.click()
        # price_max.send_keys("20000")
        # results = WebDriverWait(self, 10).until(
        #     EC.element_to_be_clickable((By.CLASS_NAME, "submit-button")))
        # results.click()
        #
        # self.driver.execute_script("window.open('');")
        # self.driver.switch_to.window(self.driver.window_handles[-1])
