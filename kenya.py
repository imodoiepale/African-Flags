
import turtle
from turtle import *


t= turtle.Turtle()

t.pensize(2)

t.penup()
t.goto(-450,250)
t.pendown()
t.color("black")
t.begin_fill()
t.forward(800)
t.right(90)
t.forward(140)
t.right(90)
t.forward(800)
t.end_fill()

t.pensize(1)
t.left(90)
t.forward(45)
t.left(90)
t.forward(800)
t.left(90)
t.forward(45)
t.left(180)

t.pensize(2)
t.penup()
t.goto(350,65)
t.pendown()
t.color("red")
t.begin_fill()
t.forward(140)
t.right(90)
t.forward(800)
t.right(90)
t.forward(140)
t.end_fill()

t.pensize(1)
t.penup()
t.goto(-450,-75)
t.pendown()
t.color("black")
t.right(180)
t.forward(45)
t.left(90)
t.forward(800)
t.left(90)
t.forward(45)
t.left(180)

t.pensize(2)
t.penup()
t.goto(350, -120)
t.pendown()
t.color("green")
t.begin_fill()
t.forward(140)
t.right(90)
t.forward(800)
t.right(90)
t.forward(140)
t.end_fill()




t.speed(0)
t.color("red")
t.penup()
t.goto(-40,155)
t.pendown()

#KENYAN SEAL

t.pensize(3)

t.penup()

t.begin_fill()

t.right(135)
t.pendown()


def curve():
    for i in range(45):
        t.right(2)
        t.forward(8)
curve()
t.right(90)
curve()

t.end_fill()



#Arrows

t.color("black")
t.penup()
t.goto(-95, 67)
t.pendown()
t.left(191)

t.begin_fill()
def curve1():
    for i in range(15):
        t.left(4)
        t.forward(10)

curve1()
t.end_fill()
t.right(90)


t.penup()
t.goto(14, 66.5)
t.pendown()
t.right(264.5)

t.begin_fill()


def curve1():
    for i in range(15):
        t.right(4)
        t.forward(10)


curve1()
t.end_fill()
t.right(90)



#straight lines

t.penup()
t.goto(0, -105)
t.pendown()
t.pensize(0.5)

t.begin_fill()
t.right(220)
t.forward(85)
t.left(90)
t.forward(6.5)
t.left(90)
t.forward(88.5)
t.color("white")
t.end_fill()


t.color("black")
t.penup()
t.goto(-92, -105)
t.pendown()
t.pensize(0.5)

t.begin_fill()
t.left(135)
t.forward(87)
t.right(90)
t.forward(6.5)
t.right(90)
t.forward(98.5)
t.color("white")
t.end_fill()





#ARROWs

t.color("black")
t.penup()
t.goto(-90, 95)
t.pendown()
t.pensize(0.5)

t.begin_fill()
t.left(65)
t.forward(25)
t.left(45)
t.forward(10.5)
t.right(65)
t.forward(75)

t.right(163)
t.forward(73.5)
t.right(50)
t.forward(10.5)
t.left(50)
t.forward(27)

t.color("white")
t.end_fill()



t.color("black")
t.penup()
t.goto(0, 95)
t.pendown()
t.pensize(0.5)

t.begin_fill()
t.left(110)
t.forward(25)
t.left(55)
t.forward(10.5)
t.right(70)
t.forward(75)

t.right(163)
t.forward(73.5)
t.right(50)
t.forward(10.5)
t.left(45)
t.forward(32)

t.color("white")
t.end_fill()
t.color("black")




#inside the shield


t.penup()
t.goto(-42, -35)
t.pendown()

t.pensize(2)
t.begin_fill()
t.color("white")
t.right(85)

def curve3():
    for i in range(9):
        t.right(12)
        t.forward(7)


curve3()

t.end_fill()
t.begin_fill()
t.color("white")

t.penup()
t.goto(-45,-35 )
t.pendown()

def curve4():
    for i in range(5):
        t.left(18.5)
        t.forward(13.225)

curve4()
t.end_fill()

#mini shields


t.penup()
t.goto(-48, 15)
t.pendown()
t.pensize(2)
t.speed(100)

t.begin_fill()
t.color("white")
t.right(10)





def curve1():
    for i in range(6):
        t.right(10)
        t.forward(22)


curve1()

t.right(155)
t.forward(130)

t.end_fill()

t.penup()
t.goto(-48, -155)
t.pendown()
t.pensize(2)
t.speed(100)

t.begin_fill()
t.color("white")
t.right(145)


def curve1():
    for i in range(6):
        t.right(10)
        t.forward(22)


curve1()

t.right(155)
t.forward(130)

t.end_fill()


t.penup()
t.goto(-43, 139)
t.pendown()
t.pensize(2)
t.speed(100)

t.right(325)
t.begin_fill()

def curve1():
    for i in range(6):
        t.right(10)
        t.forward(22)


curve1()

t.right(155)
t.forward(130)
t.end_fill()


t.penup()
t.goto(-43, -35)
t.pendown()
t.pensize(2)
t.speed(100)

t.right(145)
t.begin_fill()


def curve1():
    for i in range(6):
        t.right(10)
        t.forward(22)


curve1()

t.right(155)
t.forward(130)
t.end_fill()

mainloop()
