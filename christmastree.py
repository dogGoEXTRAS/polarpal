import turtle as t
from turtle import Turtle

def christmasTree(): 
    a = Turtle()

    a.screen.title('Christmas Tree Art by PolarPal A.I.')

    t.color('#3C5548')
    t.bgcolor('#D2E3F0')

    t.penup()
    t.goto(-100, -150)
    t.pendown()

    t.begin_fill()
    t.fd(200)
    t.bk(200)

    t.lt(65)
    t.fd(150)

    t.rt(65)
    t.fd(135)

    t.rt(65)
    t.fd(153)
    t.end_fill()

    t.penup()
    t.bk(100)
    t.pendown()

    t.begin_fill()
    t.lt(65)
    t.fd(20)
    t.bk(230)

    t.lt(65)
    t.fd(100)

    t.rt(65)
    t.fd(160)

    t.rt(65)
    t.fd(100)

    t.end_fill()

    t.begin_fill()

    t.bk(75)
    t.lt(65)
    t.fd(20)

    t.bk(220)
    t.lt(65)
    t.fd(265)
    t.rt(130)
    t.fd(270)
    t.lt(65)
    t.bk(30)

    t.end_fill()

    t.color('#5c2b2b')

    t.penup()
    t.goto(10, -150)
    t.pendown()

    t.begin_fill()

    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(105)

    t.end_fill()

    t.penup()
    t.goto(15, -100)
    t.pendown()

    t.color('red')

    t.begin_fill()

    for _ in range(360): 
        t.fd(0.3)
        t.rt(1)

    t.end_fill()

    t.penup()
    t.goto(15, -25)
    t.pendown()

    t.color('yellow')

    t.begin_fill()

    for _ in range(360): 
        t.fd(0.3)
        t.rt(1)

    t.end_fill()

    t.penup()
    t.goto(15, 50)
    t.pendown()

    t.color('blue')

    t.begin_fill()

    for _ in range(360): 
        t.fd(0.3)
        t.rt(1)

    t.end_fill()

    t.penup()
    t.goto(85, 265)
    t.lt(90)
    t.pendown()

    t.color('yellow')

    t.begin_fill()

    for _ in range(5): 
        t.fd(100)
        t.lt(144)

    t.end_fill()

    t.hideturtle()

    a.screen.mainloop()