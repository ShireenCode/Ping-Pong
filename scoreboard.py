from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
