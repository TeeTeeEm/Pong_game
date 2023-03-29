from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle()
paddle_l = Paddle()

ball = Ball()
scoreboard = ScoreBoard()

paddle_r.goto(350, 0)
paddle_l.goto(-350, 0)

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")
true = True
x = 0.1
while true:
    scoreboard.update_score()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        x -= 0.005
    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        x = 0.1
        scoreboard.add_l()

    if ball.xcor() < -380:
        ball.refresh()
        x = 0.1
        scoreboard.add_r()

screen.exitonclick()
