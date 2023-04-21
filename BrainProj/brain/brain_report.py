from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import re


class BrainReport:
    def __init__(self, list_section_element: WebElement):
        self.list_section_element = list_section_element
        self.deal_list = self.pull_deal_list()
        self.SELECTORS = {
            'name': 'h3[class="br-pp-desc br-pp-ipd-hidden "]',


        }

    def pull_deal_list(self):
        return self.list_section_element.find_elements(By.CSS_SELECTOR,
                                                       'div[class="col-lg-3 col-md-4 col-sm-6 col-xs-6 '
                                                       'product-wrapper br-pcg-product-wrapper"]')

    def pull_titles(self):
        collection = []

        def remove_serial_nr(name):
            pattern = "(?P<serial_nr>\([^\)]*\))"
            match = re.search(pattern, name)
            if match:
                return name.replace(match['serial_nr'], '')
            else:
                return name

        for deal_box in self.deal_list:
            name = deal_box.find_element(By.CSS_SELECTOR, self.SELECTORS['name']).get_attribute("textContent").strip()

            name_item = remove_serial_nr(name)
            price_item = deal_box.find_element(By.CSS_SELECTOR,
                                               'span[itemprop="price"]').get_attribute(
                "textContent").strip()
            star_item = deal_box.find_element(By.CSS_SELECTOR,
                                              'div[class="br-pp-r"]').get_attribute(
                "textContent").strip()

            collection.append(
                [name_item, price_item, star_item]
            )
        return collection
