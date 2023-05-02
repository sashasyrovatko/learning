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


tim.speed("normal")

# for _ in range(200):
#     tim.color(random_color())
#     tim.circle(50)
#     tim.circle(50, 360)
#     tim.left(10)


# Angela
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        # current_heading = tim.heading()
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(1)

screen = Screen()
screen.exitonclick()