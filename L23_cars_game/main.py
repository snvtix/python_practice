import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
board = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    if player.ycor() > player.finish:
        player.reset_pos()
        board.point()
        car_manager.speed += 1

    for car in car_manager.cars:
        if player.distance(car) < 5:
            player.reset_pos()

screen.exitonclick()