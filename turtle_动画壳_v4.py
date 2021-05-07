# 在这里写上你的代码 :-)
from  turtle import *
import math

k=1

def myFun(x,y,m):
     pu()
     goto(x,y)
     pd()
     lt(m/25) #旋转(角度制)
     fillcolor("#"+hex(0x100000+int(x*m*y) % 0xEFFFFF)[2:])  #填充色
     begin_fill()  #开始填充
     circle(20+200/(2+m*m), steps=3)
     end_fill()    #结束填充


def Draw():
    ht() #隐藏乌龟
    tracer(False) #快速直接画
    global k
    #指定区间逐一画图:
    clear()
    for m in range(-350,350,3):
        x=m;y=100*math.cos(m/150)
        myFun(x,y,m)
    update()
    k+=1
    ontimer(Draw(), 50)

Draw()
