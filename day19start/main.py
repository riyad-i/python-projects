import time
import turtle
from turtle import Turtle, Screen
from time import sleep
import random

screen = turtle.Screen()
screen.bgcolor('chocolate1')
screen.setup(1400, 900)

# make different instances, potentially want to input attributes of istance into parameters of class call

# red = Turtle()
# red.ht()
# red.penup()
# red.color('red')
# red.shape('turtle')
# red.setpos(-600, -350)
# red.shapesize(4, 4, 1)
# red.showturtle()
# red.speed(0)
#
# def set_turt(name, color, shape='turtle', y=-250):
#     name = Turtle()
#     name.ht()
#     name.color(color)
#     name.shape(shape)
#     name.penup()
#     name.setpos(-600, y)
#     name.shapesize(4, 4)
#     name.showturtle()
#     name.speed(0)
#     return name
#
#
#
# blue = set_turt('blue', 'blue', y=-250)
# yellow = set_turt('yellow', 'yellow', y=-150)
# green = set_turt('green', 'green', y=-50)
# orange = set_turt('orange', 'orange', y=50)
# purple = set_turt('purple', 'purple', y=150)
# brown = set_turt('brown', 'brown', y=250)
# aqua = set_turt('aqua', 'aqua', y=350)

colors = ['blue', 'yellow', 'green', 'red', 'orange', 'purple', 'aqua', "brown"]

y = -450

et= []

for color in colors:
    realcolor = color
    color = Turtle('turtle')
    color.ht()
    color.color(realcolor)
    color.penup()
    color.shapesize(4,4)
    color.showturtle()
    color.speed(0)
    y += 100
    color.setpos(-600, y)
    et.append(color)



#use .color to return color

def rand_walk(turt):
    r = random.randint(0, 20)
    turt.fd(r)
    #time.sleep(.01)



#turtles = {blue: 'blue', yellow: 'yellow', green: 'green', red: 'red', orange: 'orange', purple: 'purple',
           #brown: 'brown', aqua: 'aqua'}

guess = screen.textinput('Make your guess', 'Which turtle will win the race? Enter a color: ').lower()
#string_color_list = []
#for key in turtles:
    #string_color_list.append(turtles[key])

while guess not in colors: #string_color_list:
    guess = screen.textinput('Error', 'Input a valid color please').lower()

for x in range(900): #could've used while loop instead. Wouldn't have had to do else/break
    for t in et:
        rand_walk(t)
        if t.xcor() > 650:
            winner = t.color()[1]
            break
    else:
        continue
    break


# for x in range(900):
#     for t in turtles:
#         rand_walk(t)
#         if t.xcor() > 650:
#             winner = turtles[t]
#             break
#     else:
#         continue
#     break

screen.bye()

if guess == winner:
    print(f'You won! The {winner} turtle is the winner')
else:
    print(f'You lose. The {winner} turtle is the winner')

#
# def f():
#     tim.fd(20)
#
# def l():
#     tim.left(18)
#
# def r():
#     tim.right(18)
#
# def d():
#     tim.back(20)
#
# def c():
#     tim.clear()
#     tim.penup()
#     tim.setpos(0,0)
#     tim.pendown()
#     tim.seth(0)
#
# screen.listen()
# screen.onkey(f, 'Up')
# screen.onkey(l, 'Left')
# screen.onkey(r, 'Right')
# screen.onkey(d, 'Down')
# screen.onkey(c, 'c')


#screen.exitonclick()
