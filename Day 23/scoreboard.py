from turtle import Turtle

FONT = ("Courier", 14, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.scoreboard = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.scoreboard}", align=ALIGNMENT, font=FONT)

    def level_update(self):
        self.scoreboard += 1
        self.update_scoreboard()

    def game_over(self):
        game = Turtle()
        game.hideturtle()
        game.write("Game OVER", align="center", font=FONT)
        game.goto(0, -50)
        game.write(f"Level: {self.scoreboard}", align=ALIGNMENT, font=FONT)
