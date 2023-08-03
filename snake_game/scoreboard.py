from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 350)
        self.hideturtle()
        self.write(f'Score : {self.score}', align='center', font= ('courier', 24, 'normal'))

    def update(self):
        self.clear()
        self.score += 1
        self.write(f'Score : {self.score}', align='center', font=('courier', 24, 'normal'))

    def gameover(self):
        self.penup()
        self.color('white')
        self.goto(0, 0)
        self.hideturtle()
        self.write(f'Game Over.', align='center', font=('courier', 32, 'normal'))

# class Gameover(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.penup()
#         self.color('white')
#         self.goto(0, 0)
#         self.hideturtle()
#         self.write(f'Game Over.', align='center', font=('courier', 32, 'normal'))
