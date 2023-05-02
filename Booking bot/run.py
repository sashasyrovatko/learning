import time
from selenium.webdriver.common.by import By
from proj2.booking.booking import Booking
try:
    with Booking() as bot:
        bot.land_search_page()
        close_popup_button = bot.find_element(By.XPATH, '//button[@aria-label="Закрити інформацію про вхід в акаунт."]')
        if close_popup_button:
            close_popup_button.click()
        bot.change_currency(currency="USD")
        bot.select_place_to_go(input("Where you want to go ?"))
        bot.selected_dates(check_in=input("What is the check in date?"),
                           check_out='2023-04-22')
        bot.select_adults(int(input("How many people")))
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh() #A workaround to let our bot to grab the data properly
        # print(len(bot.report_results()))
        bot.report_results()


except Exception as e:
     print("Problem")




time.sleep(90)
