# SCOPE

enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function : {enemies}")

increase_enemies()
print(f"Enemies inside function : {enemies}")

#Local scope
# def drink_potion():
#      potion_strength = 2
#      print(potion_strength)
# drink_potion()
# print(potion_strength)
#NameError: name 'potion_strength' is not defined

#Global Scope
player_health = 10
def drink_potion():
    potion_strength = 2
    print(player_health)
drink_potion()
print(player_health)
#10

#There is no Block scope
#if 3 > 2:
    # if you create a variable within a function,then it's only available within that function.
    # But if you create a variable within an if block or a while loop or a for loop or anything
    # that has the indentation and the colon,then that does not count as creating a separate local
    # scope.
 #Modifying Global Scope
enemies = 1
def increase_enemies():
    #global enemies
    #enemies += 1
    print(f"enemies inside function : {enemies}")
    return enemies + 5


enemies = increase_enemies()
print(f"Enemies inside function : {enemies}")
