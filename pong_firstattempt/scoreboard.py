from turtle import Turtle

user = 0
comp = 0
FONT_SIZE = 80

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-130, 300)
        self.write(user, align='left', font=('courier', FONT_SIZE, 'normal'))
        self.goto(100, 300)
        self.write(comp, align='left', font=('courier', FONT_SIZE, 'normal'))

    def refresh(self):
        self.clear()
        self.goto(-130, 300)
        self.write(user, align='left', font=('courier', FONT_SIZE, 'normal'))
        self.goto(100, 300)
        self.write(comp, align='left', font=('courier', FONT_SIZE, 'normal'))

