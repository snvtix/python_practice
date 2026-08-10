from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.speed = 0
        
    def create_car(self):
        if random.randint(1,3) == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(280, random.randrange(-250, 250, 30))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE - (self.speed*MOVE_INCREMENT))
