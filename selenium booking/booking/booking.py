from selenium import webdriver
import proj2.booking.constance as const
import os
from selenium.webdriver.common.by import By
from proj2.booking.bookingFiltr import BookingFiltration
from booking_report import BookingReport
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\selenium", teardown=False):

        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_search_page(self):
        self.get(const.BASE_URL)

    def search_page(self):
        search = self.find_element(By.CLASS_NAME, "btn-search")
        search.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, ":Ra9:")
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_result = self.find_element(By.XPATH,
                                         '//*[@id="indexsearch"]/div[2]/div/div/form/div[1]/div[1]/div/div/div[2]/ul/li[2]/div/div/div/div[1]')
        first_result.click()
    # def selected_dates(self, check_in, check_out):
    #     check_in_element = self.find_element(By.CSS_SELECTOR,
    #                                          f"td[data-date={check_in}]"
    #                                          )
    #     check_in_element.click()
    #     check_out_element = self.find_element(By.CSS_SELECTOR,
    #                                           f"td[data-date={check_out}]")
    #     check_out_element.click()
    def select_adults(self,count=1):
        selection_element = self.find_element(By.ID,
                                              'occupancy-config')
        selection_element.click()
        while True:
            decrease_adults_element = self.find_element(By.CSS_SELECTOR,
                                                       'button[aria-label="Decrease number of Adults"]'
                                                       )
            decrease_adults_element.click()
            #If the value of adults reaches 1,then we should get out
            #of the while loop
            adults_value_element = self.find_element(By.ID, "group_adults")
            adults_value = adults_value_element.get_attribute("value")
            #Should give back the adults count
            if int(adults_value) == 1:
                break
        increase_button_element = self.find_element(By.CSS_SELECTOR,
                                                    'button[aria-label="Increase number of Adults"]'
                                                    )
        for i in range(count - 1):
            increase_button_element.click()


    def click_search(self):
         search_button = self.find_element(By.CSS_SELECTOR,
                                           'button[type="submit"]'
                                           )
         search_button.click()


    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR,
                                             "button[aria-label='Ціни в Українська гривня']")
        currency_element.click()

        selected_currency_element = self.find_element(By.XPATH,
                                                      "//*[@id='b2indexPage']/div[22]/div/div/div/div/div[2]/div/"
                                                      "div[1]/div/div/ul[1]/li[2]"
                                                      )
        selected_currency_element.click()


    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(5)
        filtration.sort()

    def report_results(self):
        hotel_box = self.find_element(By.ID,
                                      'search_results_table')
            #.find_element(By.CSS_SELECTOR,'data-testid["property-card"]')

        report = BookingReport(hotel_box)
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_row(report.pull_deal_box_attrributes())
        # print(report.pull_deal_box_attrributes())
        print(table)


