# 在这里写上你的代码 :-)
from turtle import *
from mouseData import *


def Trgl1(x,y):
    pu()
    goto(x,y)
    pd()
    color("red")  #画笔颜色
    circle(4)

def Trgl2(x,y):
    pu()
    goto(x,y)
    pd()
    color("blue")  #画笔颜色
    circle(3, steps=4)

def Trgl3(x,y):
    pu()
    goto(x,y)
    pd()
    color("green")  #画笔颜色
    circle(4, steps=3)

def Draw():
    ht() #隐藏乌龟
    tracer(False) #快速直接画

    #指定区间逐一画图1:
    for i in range(0,len(L1)-1,2):
        Trgl1(L1[i],L1[i+1])

    #指定区间逐一画图2:
    for i in range(0,len(L2)-1,2):
        Trgl2(L2[i],L2[i+1])

    #指定区间逐一画图3:
    for i in range(0,len(L3)-1,2):
        Trgl3(L3[i],L3[i+1])

Draw()
