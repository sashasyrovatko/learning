import random
from turtle import Turtle, Screen
import turtle as t
tim = Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple


directions = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("normal")
for _ in range(200):
    tim.color(random_color())
    # tim.color(random.choice(color))
    tim.forward(30)
    tim.setheading(random.choice(directions))


# color = ["blue", "dark slate gray", "gold", "red", "green", "pink", "medium purple"]
tim.shape("turtle")
tim.color("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# for _ in range(8):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown



# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3 ,11):
#     tim.color(random.choice(color))
#     draw_shape(shape_side_n)

#
# def random_walk():
#






# My
# go = True
# while go:
#     tim.pensize(10)
#     tim.color(random.choice(color))
#     tim.forward(random.randint(30, 50))
#     tim.right(random.randint(90, 180))










screen = Screen()
screen.exitonclick()