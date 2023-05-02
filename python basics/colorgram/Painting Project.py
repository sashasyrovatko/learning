# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('art.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#     # rgb_colors.append(color.rgb)
import random
from turtle import Screen
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(235, 229, 99), (18, 114, 167), (163, 80, 48), (208, 159, 92), (186, 13, 63), (131, 180, 201),
              (230, 78, 49), (36, 137, 84), (7, 35, 89), (148, 163, 37), (76, 41, 22), (166, 48, 91), (113, 186, 165),
              (223, 120, 149), (20, 169, 208), (62, 159, 92), (215, 72, 118), (8, 94, 52), (238, 163, 191),
              (95, 21, 68), (147, 205, 223), (213, 223, 9), (12, 87, 107), (247, 170, 146), (11, 46, 125),
              (160, 211, 188)]
tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
up = True

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = Screen()
screen.exitonclick()
