# coding=cp936
import math
import turtle
from datetime import *  

#t=0
def Tick():
    #global t
    # 绘制表针的动态显示
    dt = datetime.today()

    #t = dt.second + dt.microsecond * 0.000001
    t = dt.microsecond * 0.001
    turtle.tracer(False)
    x=400*math.cos(t)
    y=300*math.sin(t)
    turtle.goto(0,0)
    turtle.goto(x,y)
    turtle.dot()

    # 100ms后继续调用tick
    turtle.ontimer(Tick, 5)

Tick()

