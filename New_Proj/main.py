import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from New_Proj.bot import Table
from selenium.webdriver.remote.webelement import WebElement

class ReadCsv(Table):
    def __init__(self, list_section_element: WebElement):
        super().__init__()
        self.data = pandas.read_csv("file.csv")
        self.list_all_elements = list_section_element
        self.elements_of_list = self.full_list()
        for url in self.data.url:
            url_1 = self.get(url)

    def full_list(self):
        return self.list_all_elements.find_elements(By.CSS_SELECTOR,
                                                       "tbody")


    def pull_titles(self):
        collection = []
        for deal_box in self.elements_of_list:
            name = deal_box.find_element(By.CSS_SELECTOR, "a").get_attribute("textContent").strip()

            collection.append(
                [name]
            )
        return collection









