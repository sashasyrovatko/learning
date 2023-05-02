import time
from selenium.webdriver.common.by import By
from booking.trip import Booking

with Booking() as bot:
    bot.land_search_page()
    # close_popup_button = bot.find_element(By.XPATH, '//button[@aria-label="Закрити інформацію про вхід в акаунт."]')
    # if close_popup_button:
    #     close_popup_button.click()
    bot.search_page()
    # bot.change_currency(currency="USD")
    bot.select_tour("Весняні Карпати")
    # bot.categoriya("Говерла")


time.sleep(90)