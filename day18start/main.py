from math import pi
import turtle
import random
from turtle import Turtle, exitonclick, Screen
timmy = Turtle()
richard = Turtle()
screen = Screen()
screen.setup(1400,900)
screen.bgcolor('white')
timmy.shape('turtle')
timmy.color('orange')
timmy.speed(0)
turtle.tracer(0,0)
# for i in range(360):
#     #timmy.begin_fill()
#     timmy.penup()
#     timmy.forward(250)
#     timmy.pendown()
#     timmy.circle(150)
#     timmy.penup()
#     timmy.back(250)
#     timmy.right(1)
#     #timmy.end_fill()
#
# turtle.update()


# def shape(sides):
#     timmy.begin_fill()
#     for num in range(sides):
#         right = 360/sides
#         timmy.forward(80)
#         timmy.right(right)
#     timmy.end_fill()
# shape(15)

# timmy.penup()
# timmy.goto(-800,0)
# timmy.pendown()
# for i in range(35):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# screen.colormode(255)
# timmy.width(3)
# def rand():
#     return random.randint(0,255)
#
# def shapes():
#     for num in range(3,42):
#         timmy.pencolor((rand(),rand(),rand()))
#         for i in range(num):
#             timmy.forward(100)
#             timmy.right(360/num)
# shapes()
# timmy.width(4)
#
# def e():
#     while True :
#         timmy.seth(90)
#         timmy.forward(10)
#         if random.randint(1, 12):
#             return
#         else:
#             return
# def w():
#     while True:
#         timmy.seth(180)
#         timmy.forward(10)
#         if random.randint(1, 12):
#             return
#         else:
#             return
# def n():
#     while True:
#         timmy.seth(270)
#         timmy.forward(10)
#         if random.randint(1, 12):
#             return
#         else:
#             return
# def s():
#     while True:
#         timmy.seth(0)
#         timmy.forward(10)
#         if random.randint(1, 12):
#             return
#         else:
#             return


# random.randint(1,2)
# def rand_walk():
#     while True:
#         timmy.width(10)
#         timmy.pencolor(random.random(),random.random(),random.random())
#         choice = random.choice([0,90,180,270])
#         timmy.seth(choice)
#         timmy.forward(25)
#         turtle.update()
#
# rand_walk()



def spiro(num):
    for _ in range(num+1):
        timmy.pencolor(random.random(),random.random(),random.random())
        timmy.circle(200)
        timmy.right(360/num)


spiro(50)

exitonclick()