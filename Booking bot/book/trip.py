from selenium import webdriver
import trip.constance as const
import os
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\selenium", teardown=False):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(150)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_search_page(self):
        self.get(const.BASE_URL)

    def search_page(self):
        search = self.find_element(By.CLASS_NAME, "btn-search")
        search.click()

    def select_tour(self, place_to_go):
        search_field = self.find_element(By.ID, "text_search")
        search_field.clear()
        search_field.send_keys(place_to_go)

    # def categoriya(self, choice=None):
    #     trip = self.find_element(By.CLASS_NAME, "multiselect")
    #     trip.click()
    #     trip.send_keys(choice)
    #     first_result = self.find_element(By.XPATH,
    #                                      "//span[data-selected='Натисніть для вибору']")
    #
    #     first_result.click()

    # def change_currency(self, currency=None):
    # """Change_currency"""
    #     currency_element = self.find_element(By.CSS_SELECTOR,
    #                                          "button[data-tooltip-text='Choose your currency']"
    #                                          )
    #     currency_element.click()
    #
    #     selected_currency_element = self.find_element(By.CSS_SELECTOR,
    #                                                  f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
    #                                                   )
    #     selected_currency_element.click()
