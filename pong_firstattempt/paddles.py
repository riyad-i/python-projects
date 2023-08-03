import turtle
from turtle import Turtle, Screen


LEFT = 180
UP = 90
RIGHT = 0
DOWN = 270

WIDTH = 20
HEIGHT = 100

MOVE_DISTANCE = 100

screen = Screen()


class UserPaddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-600, 0)
        self.draw_paddle()

    def draw_paddle(self, y=0):
        self.clear()
        self.penup()
        self.sety(y)
        self.pendown()
        self.begin_fill()
        self.fd(WIDTH)
        self.left(90)
        self.fd(HEIGHT)
        self.left(90)
        self.fd(WIDTH)
        self.left(90)
        self.fd(HEIGHT)
        self.left(90)
        self.end_fill()

    def up(self):
        y = self.ycor()
        y += MOVE_DISTANCE
        self.draw_paddle(y)

    def down(self):
        y = self.ycor()
        y -= MOVE_DISTANCE
        self.draw_paddle(y)


class CompPaddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(600, 0)
        self.draw_paddle()

    def draw_paddle(self, y=0):
        self.clear()
        self.penup()
        self.sety(y)
        self.pendown()
        self.begin_fill()
        self.fd(WIDTH)
        self.left(90)
        self.fd(HEIGHT)
        self.left(90)
        self.fd(WIDTH)
        self.left(90)
        self.fd(HEIGHT)
        self.left(90)
        self.end_fill()

    def up(self):
        y = self.ycor()
        y += MOVE_DISTANCE
        self.draw_paddle(y)

    def down(self):
        y = self.ycor()
        y -= MOVE_DISTANCE
        self.draw_paddle(y)

