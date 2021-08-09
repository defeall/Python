from turtle import *
import turtle
t=turtle.Turtle()
def jump(distanz, winkel=0):
    global number
    t.penup()
    t.right(winkel)
    t.forward(distanz)
    t.left(winkel)
    t.pendown()
t.pensize(7)
rad=100
abc=19
bcd=19
number=1
for j in range(10):
    for i in range(abc):
        jump(rad)
        t.write(str(number),align="center")
        jump(-rad)
        t.rt(bcd)
        number=number+1
    rad=rad-10
    abc=abc-2
    bcd=bcd+2
    number
turtle.ht()    
