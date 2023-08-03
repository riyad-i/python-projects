from turtle import Turtle, Screen
import random
import scoreboard
import time
from paddles import UserPaddle, CompPaddle

score = scoreboard.Score()

class Ball(Turtle):

    is_left = random.randint(0, 1)
    is_ypos = random.randint(0, 1)
    xspeed = random.randint(5, 9)
    yspeed = random.randint(1, 4)

    refreshed = False
    # is_left = True
    # is_ypos = True

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        #self.hideturtle()
        self.penup()
        Screen().update()
        time.sleep(.5)

    def strafe_left(self):
        x = self.xcor()
        y = self.ycor()
        if self.is_ypos:
            y += self.yspeed
        else:
            y -= self.yspeed
        x -= self.xspeed
        self.setx(x)
        self.sety(y)

    def strafe_right(self):
        x = self.xcor()
        y = self.ycor()
        if self.is_ypos:
            y += self.yspeed
        else:
            y -= self.yspeed
        x += self.xspeed
        self.setx(x)
        self.sety(y)

    def check_left(self, ux, uy):
        #print(f'ball.xcor ={self.xcor()}')
        if self.xcor() - 33 < ux and (uy - 10 < self.ycor() < uy + 110):
            self.is_left = False
            self.is_ypos = random.randint(0, 1)
            self.xspeed = random.randint(8, 15)
            self.yspeed = random.randint(1, 8)
            return False
        return True

    def check_right(self, cx, cy):
        if self.xcor() + 13 > cx and cy - 10 < self.ycor() < cy + 110:
            self.is_left = True
            self.is_ypos = random.randint(0, 1)
            self.xspeed = random.randint(8, 15)
            self.yspeed = random.randint(1, 8)
            return False
        return True

    def check_ceil(self):
        if self.ycor() > 387:
            self.is_ypos = False
        if self.ycor() < -380:
            self.is_ypos = True

    def past_paddle(self, ux, cx):
        if self.xcor() - 10 < ux:
            scoreboard.comp += 1  # reset
            self.is_left = random.randint(0, 1) #buggy
            #self.refreshed = True
            self.is_ypos = random.randint(0, 1)
            self.xspeed = random.randint(8, 15)
            self.yspeed = random.randint(1, 8)
            self.reset_ball()
            score.refresh()

        if self.xcor() - 10 > cx:
            scoreboard.user += 1
            self.is_left = random.randint(0, 1)
            #self.refreshed = True
            self.is_ypos = random.randint(0, 1)
            self.xspeed = random.randint(8, 15)
            self.yspeed = random.randint(1, 8)
            self.reset_ball()
            score.refresh()

    def reset_ball(self):
        self.clear()
        self.goto(0,0)
        Screen().update()
        time.sleep(.5)
