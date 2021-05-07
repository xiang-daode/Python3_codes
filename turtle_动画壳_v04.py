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
    for m in range(-350,350,15):
        x=250*math.cos(m/60)
        y=250*math.sin(m/48)
        #线段集:
        pu();
        goto(0,0);
        #goto(x,y);
        #goto(x*math.cos(k/48)-y*math.sin(k/48),x*math.sin(k/48)+y*math.cos(k/48))
        pencolor("#"+hex(0x100000+(m**2) % 0xEFFFFF)[2:]);pensize(4)
        pd();goto(x*math.cos(k/37)-y*math.sin(k/37),x*math.sin(k/37)+y*math.cos(k/37))
        #填充多边形:
        begin_fill()
        lt(1)
        fillcolor("#"+hex(0x100000+(m**4) % 0xEFFFFF)[2:])
        circle(25,steps=3)
        end_fill()
    #画图结束-----------------------------

    update() #<<=====更新画布=====
    k+=1 #<<=====变量递增=====
    ontimer(DrawLoop(), 50) #<<=====每隔n毫秒循环执行=====


ht() #隐藏乌龟
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====
