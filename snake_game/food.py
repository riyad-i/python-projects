from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.dot()
        self.xcoord = random.randint(-375, 375)
        self.ycoord = random.randint(-375, 375)
        self.dot.hideturtle()
        self.dot.penup()
        self.dot.goto(self.xcoord, self.ycoord)
        self.dot.dot(13, "white")