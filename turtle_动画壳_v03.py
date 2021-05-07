# 在这里写上你的代码 :-)
from  turtle import *
import math
import sys

#修改最大递归层数到0xffffff
sys.setrecursionlimit(0xffffff)


k=1 #<<====全局变量======

def DrawLoop():
    global k #<<====全局变量======
    clear() #<<=====清空画布=====

    #画图开始:-----------------------------
    for m in range(-350,350,2):
        x=300*math.cos(m/48)
        y=200*math.sin(m/36)
        goto(x*math.cos(k/48)-y*math.sin(k/48),x*math.sin(k/48)+y*math.cos(k/48))
        color("black", "#5588FF")
        begin_fill()
        lt(1)
        circle(25,steps=3)
        end_fill()
    #画图结束-----------------------------

    update() #<<=====更新画布=====
    k+=1 #<<=====变量递增=====
    ontimer(DrawLoop(), 50) #<<=====每隔n毫秒循环执行=====


ht() #隐藏乌龟
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====
