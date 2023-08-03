import random
import turtle
from turtle import Turtle, Screen
from paddles import UserPaddle, CompPaddle
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.setup(1400, 800)
screen.bgcolor('black')
turtle.tracer(0)
screen.listen()

user_paddle = UserPaddle()
comp_paddle = CompPaddle()

ux = user_paddle.xcor()
cx = comp_paddle.xcor()
screen.update()
ball = Ball()

#for a reset, use time.sleep to have ball sit in middle for a sec, than shoot out


while True:
    uy = user_paddle.ycor()
    cy = comp_paddle.ycor()
    screen.onkeypress(user_paddle.up, 'w')
    screen.onkeypress(user_paddle.down, 's')
    screen.onkeypress(comp_paddle.up, 'Up')
    screen.onkeypress(comp_paddle.down, 'Down')
    if ball.is_left:
        if ball.check_left(ux, uy): # ball boolean left right
            ball.strafe_left()
    elif ball.check_right(cx, cy):
        ball.strafe_right()
    ball.check_ceil()
    ball.past_paddle(ux, cx)
    turtle.update()




screen.exitonclick()