from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def backwards():
    tim.back(10)


def counter_clockwise():
    tim.right(20)


def clockwise():
    tim.circle(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(backwards, "S")
screen.onkey(counter_clockwise, "A")
screen.onkey(clockwise, "D")
screen.onkey(clear, "C")
screen.onkey(move_forwards, "W")
screen.exitonclick()
