import turtle
import copy
import time
from turtle import Screen, Turtle
from snake import Snake
from snake import Dot
import food
from scoreboard import Scoreboard #Gameover

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Snake Game')
screen.listen()

#et = []

# x = 40
# coords = [(0, 0), (-30, 0), (-60, 0)]

screen.tracer(0)

# for pos in coords:
#     turt_obj = Turtle('square')
#     turt_obj.penup()
#     turt_obj.color('white')
#     turt_obj.setpos(pos)
#     # x -= 20
#     et.append(turt_obj)




game_is_on = True

mycoords = [(0, -200), (-20, -200), (-40, -200)]
snake = Snake(coords=mycoords)


dotval = False
scoreboard = Scoreboard()

while game_is_on:
    snake.screen.update()
    snake.move()
    if not snake.check_bound():
        break
    time.sleep(snake.sleep_timer)
    Snake.screen.listen()
    turtle.onkeypress(snake.left, 'Left')
    turtle.onkeypress(snake.right, 'Right')
    turtle.onkeypress(snake.up, 'Up')
    turtle.onkeypress(snake.down, 'Down')
    turtle.onkeypress(snake.speed_up, 'space')
    if dotval == False:
        dot = Dot()
        dotval = True
    if dot.check_coord(): #return true or false
        dotval = False
        scoreboard.update()
        snake.add_obj()

scoreboard.gameover()





# def left():
#     et[0].seth(180)
#
# def right():
#     et[0].seth(0)
#
# def up():
#     et[0].seth(90)
#
# def down():
#     et[0].seth(270)


screen.update()

# while game_is_on:
#     screen.update()
#     screen.listen()
#     turtle.onkeypress(left, 'Left')
#     turtle.onkeypress(right, 'Right')
#     turtle.onkeypress(up, 'Up')
#     turtle.onkeypress(down, 'Down')
#     # for x in range(2, -1, -1):
#     #     #time.sleep(.5)
#     #     et[x].fd(20)
#     #     screen.update()
#     #     if x == 0:
#     #         break
#     #     if et[x-1].heading() != et[x].heading():
#     #         et[x].seth(et[x-1].heading())
#     for x in range(len(et) - 1, 0, -1):
#         time.sleep(.015)
#         new_x = et[x - 1].xcor()
#         new_y = et[x - 1].ycor()
#         et[x].setpos(new_x, new_y)
#     et[0].fd(20)






# while game_is_on:
#     screen.update()
#     time.sleep(.1)
#     for obj in reversed(et):
#         obj.fd(10)
#     et[0].left(90)
#     for x in range(len(et)):
#         # if et[x] == et[0]:
#         #     continue
#         if x == len(et)-1:
#             continue
#         if et[x+1].heading() != et[x].heading():
#             et[x+1].seth(et[x].heading())
#         screen.update()























screen.exitonclick()


# y = 0
# def left():
#     # for turt in et:
#     #     turt.left(90)
#     xval = et[0].xcor()
#     # while turt.xcor() in et < xval:
#     #     fd(5)
#     et[0].left(90)
#     switch_list = []
#     for tu in et:
#         if tu == et[0]:
#             continue
#         while tu.xcor() < xval:
#             tu.fd(5)
#         tu.left(90)
#         distance = et.index(tu) * 20
#         switch_list.append(distance)
#         # tu.fd(distance)
#     for tu in et:
#         tu.fd(switch_list.pop())
        # while t.xcor() < xval:
        #     print(xval)
        #     print(t.xcor)
        #     t.fd(1)
        # print(xval)
        # print(t.xcor())
        # t.left(90)


# define a function to see direction of snake ie.seth
# from there make function for all directions, and make higherorder function with direction passing as parameters


# def coords():
#     print(et[0].pos())


# while True:
#     for turt in et:
#         turt.fd(5)
#         turtle.onkeypress(left, 'Left')

        # xval = et[0].xcor()
        # if turt.xcor() == 200:
        #     turt.left(90)

        # if turt.xcor() == 200 and turt.heading() == 0:
        #     turt.left(90)
        # if turt.ycor() == 200 and turt.heading() == 90:
        #     turt.left(90)
        # if turt.xcor() == -200 and turt.heading() == 180:
        #     turt.left(90)
        # if turt.ycor() == -200 and turt.heading() == 270:
        #     turt.left(90)

