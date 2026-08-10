from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

l_paddle = Paddle(350,0)
r_paddle = Paddle(-350,0)
board = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_is_on = True

while game_is_on == True:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() < -320) or (ball.distance(l_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_x()

    if ball.xcor() > 385:
        board.r_point()
        ball.reset_pos()
    elif ball.xcor() < -385:
        board.l_point()
        ball.reset_pos()

screen.exitonclick()