# # import turtle
# from turtle import Turtle, Screen, screensize, setup,circle
#
# timmy = Turtle()
# # print(timmy)
# richard= Turtle()
#
# my_screen = Screen()
# my_screen.canvheight = 300
# setup(1350,1050)
# screensize(canvwidth=400, canvheight=400,
#                   bg="blue")
# timmy.shape('square')
# timmy.color('chocolate')
# richard.shape('turtle')
# richard.setx(30)
# richard.sety(45)
# richard.color('seagreen')
# richard.forward(200)
# timmy.back(250)
# timmy.begin_fill()
# timmy.circle(300)
# timmy.end_fill()
# my_screen.exitonclick()
#

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align='l'
print(table)


