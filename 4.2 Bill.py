import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# # names = ["Angella", "Bill", "Ema", "Nevil","David"]
# num_items = len(names)
# random_name = random.randint(0, num_items - 1)
# # print(random_name)
# person_who_will_pay = names[random_name]
# print(person_who_will_pay)

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today")
