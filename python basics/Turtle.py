# import turtle
# timmy = turtle.Turtle()
# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# # <turtle.Turtle object at 0x000001EDBC423FD0>
# my_screen = Screen()
# print(my_screen.canvheight)
# # 300
# my_screen.exitonclick()
# pypi.org
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
