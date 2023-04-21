import time
from BrainProj.brain.brain import Brain


inst = Brain()
inst.search_page()
inst.city_choice(input("Choice city\n"))
time.sleep(5)
inst.search_element(input("What are you looking for?\n"))
inst.categories(input("Price from?\n"), input("Price to?\n"))
inst.refresh()
inst.report_results()
