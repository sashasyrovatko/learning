from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_all = []
        self.create_snake()
        self.head = self.snake_all[0]

    def create_snake(self):
        for snake_index in START_POS:
            self.add_segment(snake_index)

    def add_segment(self, snake_index):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(snake_index)
        self.snake_all.append(snake)

    def reset(self):
        for seg in self.snake_all:
            seg.goto(1000, 1000)
        self.snake_all.clear()
        self.create_snake()
        self.head = self.snake_all[0]

    def extend(self):
        self.add_segment(self.snake_all[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_all) - 1, 0, -1):
            new_x = self.snake_all[seg_num - 1].xcor()
            new_y = self.snake_all[seg_num - 1].ycor()
            self.snake_all[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

