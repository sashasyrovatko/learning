from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BrainFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_filtration(self):
        categor = self.driver.find_element(By.CSS_SELECTOR,
                                           'button[class="br-o-filter categories"]'
                                           )
        categor.click()
