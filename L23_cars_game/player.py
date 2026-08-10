from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.move_dist = MOVE_DISTANCE
        self.finish = FINISH_LINE_Y

    def move(self):
        self.forward(self.move_dist)

    def reset_pos(self):
        self.goto(STARTING_POSITION)
