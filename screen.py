from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# SCREEN
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("green")
screen.title("Pong")
screen.tracer(0)

# PADDLES
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# BALL
ball = Ball()

# SCOREBOARDS
l_score = Scoreboard((-250, 270))
r_score = Scoreboard((250, 270))

game_on = True
while game_on:
    time.sleep(0.15)
    screen.update()
    ball.move()

    # detect collisions with top and bottom walls
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()

    # detect collisions with paddles
    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.hit()
        l_score.increase_score()
    elif ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.hit()
        r_score.increase_score()

    # detect when out of bounds
    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.x_move *= -1
        l_score.increase_score()
    elif ball.xcor() < -400:
        ball.goto(0, 0)
        ball.x_move *= -1
        r_score.increase_score()
