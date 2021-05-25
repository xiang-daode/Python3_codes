# 在这里写上你的代码 :-)
from turtle import *
import math


x0,y0=0,0
u,v,w=.1,.2,.3
def Trgl(x,y,q):
    global x0,y0
    rgb="#"+hex(0x100000+(q**3) % 0xEFFFFF)[2:]
    clr="#"+hex(0x100000+(q**2) % 0xEFFFFF)[2:]
    pu()
    goto(x0,y0)
    pd()
    pensize(6)
    pencolor(rgb)
    goto(x,y)
    
    lt(.1) #旋转(角度制)
    fillcolor(clr)  #填充色
    begin_fill()  #开始填充
    circle(5+(int)(q*q/1000) % 30, steps=2+q%10)
    end_fill()    #结束填充
    x0,y0=x,y

def Draw():
    ht() #隐藏乌龟
    tracer(False) #快速直接画
    global u,v,w,x0,y0
    u,v,w=u+.01,v+.02,w+.03
    #指定区间逐一画图:
    clear()
    for q in range(-360,366,6):
        x=200*math.cos(u-q/90)+100*math.cos(v*q/150)+150*math.cos(-w+q/45)
        y=200*math.sin(u-q/60)+100*math.sin(v*q/120)+150*math.sin(-w+q/75)
        Trgl((int)(y),(int)(-x),q)
    update()
    ontimer(Draw(), 20)
    

Draw()
