# 在这里写上你的代码 :-)
import turtle
import math

k=1

def Trgl(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    #global k
    turtle.lt(k/5) #旋转(角度制)
    turtle.fillcolor("#"+hex(0x100000+(x*y)% 0xEFFFFF)[2:])  #填充色
    turtle.begin_fill()  #开始填充
    turtle.circle(60-k%50, steps=3)
    turtle.end_fill()    #结束填充


def Draw():
    turtle.ht() #隐藏乌龟
    turtle.tracer(False) #快速直接画
    global k
    #指定区间逐一画图:
    turtle.clear()
    for q in range(-350,350,5):
        x=300*math.cos(q/100)*math.sin(k/29)
        y=300*math.sin(q/100)*math.cos(k/97)
        Trgl((int)(x),(int)(y))
    turtle.update()
    k+=.1
    if k>999:
       return
    turtle.ontimer(Draw(), 50)

Draw()
