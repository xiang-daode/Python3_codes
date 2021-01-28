# coding=cp936
import math
import turtle
from datetime import *  


def Tick():
    turtle.ht()
    
    dt = datetime.today()
    turtle.clear()
    t = 2*(dt.microsecond/360000 % 3.14159265)
    turtle.tracer(False)
    x=300*math.cos(t)
    y=300*math.sin(t)
    x2=x+80*math.sin(-t)
    y2=y+80*math.cos(t)
    turtle.goto(0,0)
    turtle.dot(90)
    turtle.goto(x,y);
    turtle.goto(x2,y2);
    turtle.dot(50)
    turtle.goto(0,0)    

    # 20ms后继续调用tick
    turtle.ontimer(Tick, 5)

Tick()

