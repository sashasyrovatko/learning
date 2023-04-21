#This file will include a class with instance methods
#That will be responsible to interect with our website
#After we have some results,to applay filtrations
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration():
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.ID, "filter_group_class_:Rsq:")
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR,
                                                        '*')
        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} зірок':
                    star_element.click()

    def sort(self):
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           'button[data-id="upsort_bh"]'
                                           )
        element.click()