# coding=cp936
import math
import turtle
from datetime import *  


t=0
def Tick(t):
    #global t
    # 绘制表针的动态显示
    t=t+0.01
    turtle.bgcolor(1,1,1)
    turtle.tracer(False)
    turtle.clear()

    x=400*math.cos(t)
    y=300*math.sin(t)
    turtle.goto(0,0)
    turtle.goto(x,y)
    turtle.dot(50)

    # 100ms后继续调用tick
    turtle.ontimer(Tick(t), 100)

Tick(t)

