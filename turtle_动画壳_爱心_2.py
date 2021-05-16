# 在这里写上你的代码 :-)
from  turtle import *
import math
import sys

#修改最大递归层数到0xffffff
sys.setrecursionlimit(0xffffff)
screensize(1080, 900, "#000")
k=1 #<<====全局变量======

def DrawLoop():
    global k #<<====全局变量======
    clear() #<<=====清空画布=====


    #画图开始:-----------------------------
    for m in range(-185,185,5):
        x=m*math.cos(m/39)+50*math.cos(k/87)
        y=m*math.sin(m/39)+50*math.sin(k/87)

        #线段集:
        pu();pensize(4)
        #goto(0,0);
        goto(x,y);
        #goto(x*math.cos(k/38)-y*math.sin(k/38),x*math.sin(k/38)+y*math.cos(k/38))
        pencolor("#"+hex(0x100000+(m**4) % 0xEFFFFF)[2:]);pd()
        goto(x*math.cos(k/39)-y*math.sin(k/39),x*math.sin(k/39)+y*math.cos(k/39))

        #填充多边形:
        begin_fill()
        lt(.1)
        fillcolor("#"+hex(0x100000+(m**4) % 0xEFFFFF)[2:])
        circle( 15,steps=3)
        end_fill()
    #画图结束-----------------------------

    update() #<<=====更新画布=====
    k+=1 #<<=====变量递增=====
    ontimer(DrawLoop(), 50) #<<=====每隔n毫秒循环执行=====


ht() #隐藏乌龟
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====
