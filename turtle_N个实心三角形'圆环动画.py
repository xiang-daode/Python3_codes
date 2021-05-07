# 在这里写上你的代码 :-)
import turtle
import math


def Trgl(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.lt(3) #旋转(角度制)
    turtle.fillcolor("#"+hex(0x100000+(x*y) % 0xEFFFFF)[2:])  #填充色
    turtle.begin_fill()  #开始填充
    turtle.circle(60, steps=3)
    turtle.end_fill()    #结束填充


def Draw():
    turtle.ht() #隐藏乌龟
    turtle.tracer(False) #快速直接画

    #指定区间逐一画图:
    turtle.clear()
    for q in range(-350,350,3):
        x=300*math.cos(q/47)
        y=300*math.sin(q/47)
        Trgl((int)(x),(int)(y))
    turtle.update()
    turtle.ontimer(Draw(), 20)

Draw()
