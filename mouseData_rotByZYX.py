# 在这里写上你的代码 :-)
from mouseData import *
from  turtle import *
import math
import sys

#修改最大递归层数到0xffffff
sys.setrecursionlimit(0xffffff)
screensize(800, 600, "#FFF")
k=1 #<<====全局变量======

def DrawLoop():
    global k #<<====全局变量======
    clear() #<<=====清空画布=====

    #画图开始:-----------------------------
    #指定区间逐一画图1:
    color("red")  #画笔颜色
    for i in range(0,len(L1)-1,2):
        x0=L1[i]
        y0=L1[i+1]
        z0=100
        x1=x0*math.cos(k)-y0*math.sin(k)
        y1=x0*math.sin(k)+y0*math.cos(k)
        z1=z0

        x2=x1*math.cos(k/2)-z1*math.sin(k/2)
        y2=y1
        z2=x1*math.sin(k/2)+z1*math.cos(k/2)

        x3=x2
        y3=y2*math.cos(k/3)-z2*math.sin(k/3)
        z3=y2*math.sin(k/3)+z2*math.cos(k/3)

        pu();goto(x3,y3)
        pd();circle(3)

    #指定区间逐一画图2:
    color("green")  #画笔颜色
    for i in range(0,len(L2)-1,2):
        x0=L2[i]
        y0=L2[i+1]
        z0=0
        x1=x0*math.cos(k)-y0*math.sin(k)
        y1=x0*math.sin(k)+y0*math.cos(k)
        z1=z0

        x2=x1*math.cos(k/2)-z1*math.sin(k/2)
        y2=y1
        z2=x1*math.sin(k/2)+z1*math.cos(k/2)

        x3=x2
        y3=y2*math.cos(k/3)-z2*math.sin(k/3)
        z3=y2*math.sin(k/3)+z2*math.cos(k/3)

        pu();goto(x3,y3)
        pd();circle(3)

    #指定区间逐一画图3:
    color("blue")  #画笔颜色
    for i in range(0,len(L3)-1,2):
        x0=L3[i]
        y0=L3[i+1]
        z0=-100
        x1=x0*math.cos(k)-y0*math.sin(k)
        y1=x0*math.sin(k)+y0*math.cos(k)
        z1=z0

        x2=x1*math.cos(k/2)-z1*math.sin(k/2)
        y2=y1
        z2=x1*math.sin(k/2)+z1*math.cos(k/2)

        x3=x2
        y3=y2*math.cos(k/3)-z2*math.sin(k/3)
        z3=y2*math.sin(k/3)+z2*math.cos(k/3)

        pu();goto(x3,y3)
        pd();circle(3)

    #画图结束-----------------------------

    update() #<<=====更新画布=====
    k+=.25 #<<=====变量递增=====
    ontimer(DrawLoop(), 10) #<<=====每隔n毫秒循环执行=====


ht() #隐藏乌龟
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====
