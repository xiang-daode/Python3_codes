from turtle import *
import math
u,v,w=0.1,0.2,0.3

def Trgl(x,y,q):
    rgb="#"+hex(0x100000+(q**3) % 0xEFFFFF)[2:]
    clr="#"+hex(0x100000+(q**2) % 0xEFFFFF)[2:]
    pensize(6)
    pencolor(rgb)
    pd();    goto(x,y)
    lt(.1) #旋转(角度制)
    fillcolor(clr)  #填充色
    begin_fill()  #开始填充
    circle(5+(int)(q*q/1000) % 30, steps=2+q%10)
    end_fill()    #结束填充

def Draw():
    ht() #隐藏乌龟
    tracer(False) #快速直接画
    global u,v,w
    u,v,w=u+.01,v+.02,w+.03
    #指定区间逐一画图:
    clear()
    for q in range(-360,366,6):
        x=500*math.cos(u*q/360)*math.cos(v-q/90)*math.cos(-w+q/60)
        y=500*math.sin(w*q/360)*math.sin(v-q/90)*math.sin(-u+q/60)
        Trgl((int)(y),(int)(-x),q)
    update()
    ontimer(Draw(), 20)
Draw()
