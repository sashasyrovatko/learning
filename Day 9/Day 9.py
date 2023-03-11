programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"] )
#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary["Loop"])
# empty_dictionary{}
#Wipe an existing dictionary
# programming_dictionary{}
print(programming_dictionary)
#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)
#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
#Nesting a list in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
#Nesting dictionary in a dictionary

print(travel_log)
#Nesting Dictionary in a list
travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total visits": 12},
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total visits": 5},
]