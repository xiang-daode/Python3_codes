from turtle import *

def yin(radius, clr):
    width(3)
    color(clr)
    up()
    goto(0,-radius)
    pd()
    begin_fill()    
    circle(radius, 360)
    end_fill()

yin(100, "black")    
yin(30, "red")   
ht()




