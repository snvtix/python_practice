from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(-280, 260)
        self.write(self.score, align="center", font=FONT)

    def point(self):
        self.score += 1
        self.update_board()
