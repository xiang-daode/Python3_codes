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
        x=L1[i]
        y=L1[i+1]
        x2=x
        y2=y*math.cos(k)
        pu();goto(x2,y2)
        pd();circle(4)
    #指定区间逐一画图3:
    color("green")  #画笔颜色
    for i in range(0,len(L3)-1,2):
        x=L3[i]
        y=L3[i+1]
        x2=x
        y2=y*math.cos(k)
        pu();goto(x2,y2)
        pd();circle(4)
    #画图结束-----------------------------

    update() #<<=====更新画布=====
    k+=1 #<<=====变量递增=====
    ontimer(DrawLoop(), 10) #<<=====每隔n毫秒循环执行=====


ht() #隐藏乌龟
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====
