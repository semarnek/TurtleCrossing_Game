from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-250, 275)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=("Arial", 12, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Arial", 24, "bold"))


    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("Arial", 12, "bold"))
