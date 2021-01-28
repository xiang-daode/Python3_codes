from turtle import *

def yin(radius, color1, color2):
    width(3)
    color("black", color1)
    begin_fill()
    circle(-radius, 360)
    left(180)
    circle(1.5*radius, 360)
    end_fill()

yin(80, "black", "white")    
ht()




