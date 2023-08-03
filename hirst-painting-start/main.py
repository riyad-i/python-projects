import turtle
import colorgram
from turtle import Turtle, Screen
import random

# real_colors = []
#
# colors = colorgram.extract('img.png',45)
# for _ in colors:
#     color = _
#     rgb = (color.rgb.r, color.rgb.g, color.rgb.b)
#     real_colors.append(rgb)

real_colors = [(230, 207, 129), (25, 113, 177), (210, 66, 89), (233, 153, 89), (122, 146, 195), (140, 95, 62),
               (224, 125, 146), (224, 71, 63), (56, 185, 119), (112, 114, 182), (130, 173, 45), (240, 149, 173),
               (119, 180, 150), (25, 176, 188), (143, 214, 164), (192, 183, 225), (135, 207, 234), (12, 156, 125),
               (173, 55, 69), (105, 49, 52), (53, 60, 104), (234, 171, 158), (103, 50, 49), (74, 43, 41), (84, 37, 41),
               (46, 51, 74)]

turtle.colormode(255)
screen = Screen()
screen.setup(1400, 900)

# y = -400  # increment spawn of turtle
# for i, color in enumerate(real_colors):
#     t = Turtle()
#     t.speed(0)
#     t.setposition(-600, -400)
#     t.width(30)
#     t.pencolor(color)
#     t.sety(y)
#     y += 25
#     t.forward(100)

t = Turtle()
t.speed(0)
t.penup()
t.setposition(-600, -400)
t.forward(50)



def grid():
    t.ht()
    original_y = -400
    original_x = -600
    for i in range(10):
        original_y += 50
        t.sety(original_y + 50)
        t.setx(original_x)
        for i in range(10):
            t.dot(25, random.choice(real_colors))
            t.forward(50)

# def grid():
#     t.ht()
#     x=0
#     original_y = -400
#     original_x = -600
#     for i in range(10):
#         t.sety(original_y + 50)
#         original_y += 50
#         t.setx(original_x)
#         for i in range(10):
#             if x == len(real_colors):
#                 x = 0
#             t.dot(25, real_colors[x])
#             x+=1
#             t.forward(50)


grid()

turtle.exitonclick()

