from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(self.score_l, align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(self.score_r, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.score_l += 1
        self.update_scoreboard()

    def r_point(self):
        self.score_r += 1
        self.update_scoreboard()

