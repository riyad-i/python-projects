import turtle
from turtle import Screen, Turtle
import time
import random
from scoreboard import Scoreboard

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    screen = turtle.Screen()
    segments = []
    coordinates = [(0, 0), (-20, 0), (-40, 0)]
    sleep_timer = .06
    colour = ''

    def __init__(self, color='white', coords=coordinates):
        self.color = color
        for pos in coords:
            turt_obj = Turtle('square')
            turt_obj.penup()
            turt_obj.color(self.color)
            turt_obj.setpos(pos)
            # x -= 20
            self.segments.append(turt_obj)
        self.head = self.segments[0]
        global colour
        colour = self.color

    def retseg(self):
        return self.segments

    def check_bound(self):
        if self.head.pos()[0] > 380 or self.head.pos()[0] < -380:
            print("Don't hit the wall!")
            return False
        if self.head.pos()[1] > 380 or self.head.pos()[1] < -380:
            print("Don't hit the wall!")
            return False
        coord_list = []
        #for n, _ in enumerate(self.segments): #or for i in range(len(self.segments))
        for i in range(1, len(self.segments)):
            coord_list.append(self.segments[i].pos())
        #coord_list.pop(0)
        if self.head.pos() in coord_list:
            print("Don't hit your tail!")
            return False
        return True


    def add_obj(self):
        last_obj = self.segments[- 1]
        new_obj = Turtle('square')
        new_obj.penup()
        new_obj.color(self.color)
        new_obj.setpos(last_obj.xcor(), last_obj.ycor())
        self.segments.append(new_obj)
        # if last_obj.heading() == RIGHT:
        #     new_obj = Turtle('turtle')
        #     new_obj.penup()
        #     new_obj.color(self.color)
        #     new_obj.setpos(last_obj.xcor() - 20, last_obj.ycor())
        #     self.segments.append(new_obj)
        # if last_obj.heading() == LEFT:
        #     new_obj = Turtle('turtle')
        #     new_obj.penup()
        #     new_obj.color(self.color)
        #     new_obj.setpos(last_obj.xcor() + 20, last_obj.ycor())
        #     self.segments.append(new_obj)
        # if last_obj.heading() == DOWN:
        #     new_obj = Turtle('turtle')
        #     new_obj.penup()
        #     new_obj.color(self.color)  # random.random(), random.random(), random.random())
        #     new_obj.setpos(last_obj.xcor(), last_obj.ycor() + 20)
        #     self.segments.append(new_obj)
        # if last_obj.heading() == UP:
        #     new_obj = Turtle('turtle')
        #     new_obj.penup()
        #     new_obj.color(self.color)
        #     new_obj.setpos(last_obj.xcor(), last_obj.ycor() - 20)
        #     self.segments.append(new_obj)

    # def add_unit(self):   # attempt to add tail object
    #     newobj = Turtle('square')
    #     newobj.penup()
    #     newobj.color(Snake.colour)
    #     newobj.setpos(self.coordinates[1])
    #     self.segments.append(newobj)

    # self.segments.append(self.segments[len(self.segments)-1])

    # def b(self):
    #     return(segments[0])
    # game_is_on = True
    # while game_is_on:
    #     self.screen.update()
    #     self.screen.listen()
    #     turtle.onkeypress(left, 'Left')
    #     turtle.onkeypress(right, 'Right')
    #     turtle.onkeypress(up, 'Up')
    #     turtle.onkeypress(down, 'Down')

    def move(self):
        for x in range(len(self.segments) - 1, 0, -1):
            # time.sleep(self.sleep_timer)
            # time.sleep(self.sleep_timer)
            new_x = self.segments[x - 1].xcor()
            new_y = self.segments[x - 1].ycor()
            new_h = self.segments[x - 1].heading()
            self.segments[x].setpos(new_x, new_y)
            self.segments[x].seth(new_h)
        self.head.fd(MOVE_DISTANCE)
        self.screen.update()
        # self.segments[0].fd(10)

    def left(self):
        if self.head.heading() == 0:
            return
        self.head.seth(180)
        # for i in self.segments:
        #     i.seth(180)

    def right(self):
        if self.head.heading() == 180:
            return
        self.head.seth(0)
        # for i in self.segments:
        #     i.seth(0)

    def up(self):
        if self.head.heading() == 270:
            return
        self.head.seth(90)
        # for i in self.segments:
        #     i.seth(90)

    def down(self):
        if self.head.heading() == 90:
            return
        self.head.seth(270)
        # for i in self.segments:
        #     i.seth(270)

    def speed_up(self):
        # global MOVE_DISTANCE
        # if MOVE_DISTANCE == 20:
        #     MOVE_DISTANCE = 40
        # elif MOVE_DISTANCE == 40:
        #     MOVE_DISTANCE = 20
        # print(Snake.sleep_timer)
        if Snake.sleep_timer == .2:
            Snake.sleep_timer = .06
        elif Snake.sleep_timer == .06:
            # print(Snake.sleep_timer)
            Snake.sleep_timer = .015
            # print(Snake.sleep_timer)
        elif Snake.sleep_timer == .015:
            Snake.sleep_timer = .2


    # speed up function, space?


class Dot(Snake):

    def __init__(self):
        self.xcoord = random.randrange(-380, 380, 20)
        self.ycoord = random.randrange(-380, 380, 20)
        self.dot = Turtle()
        self.dot.hideturtle()
        self.dot.penup()
        self.dot.goto(self.xcoord, self.ycoord)
        self.dot.dot(13, "white")

    def check_coord(self):
        headx = (super().retseg()[0].pos())[0]
        heady = (super().retseg()[0].pos())[1]
        # print(headx,heady)
        # print(self.xcoord,self.ycoord)
        if self.xcoord - 12 < headx < self.xcoord + 12:
            if self.ycoord - 12 < heady < self.ycoord + 12:
                #print('you got it')
                self.dot.clear()
                # super().add_unit()  #add tail object attempt
                return True

    # def __del__(self):
    # pass

    # print(super().b())
