import random

random_integer = random.randint(1, 10)
print(random_integer)
#0.00000000 - 0.9999999
random_float = random.random()
print(random_float)
#randomFloat = random.random() * 5

#love_score = random.randint(1, 100)
#print(f"Youre love score is {love_score}")

# list on python
fruits = ["Apple", "Cherry", "Limon"]
print(fruits [2])
print(fruits[-2])
# - last item in the list
# if change name in list
fruits[1] = "Chery"
print(fruits)
#added after list .append
fruits.append("Pear")
print(fruits)
#More on list

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
               "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines"]
vegetables = ["Spinach", "Kale"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)