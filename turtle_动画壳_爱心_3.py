# 在这里写上你的代码 :-)
from  turtle import *
import math
import sys

#修改最大递归层数到0xffffff
#sys.setrecursionlimit(0xffffff)
screensize(1080, 900, "#000")
k=1 #<<====全局变量======

def DrawLoop():
    global k #<<====全局变量======
    clear() #<<=====清空画布=====


    #画图开始:-----------------------------
    for m in range(-285,285,5):
        x=200*math.cos(k/10+m/48)+50*math.cos(k/4.8)
        y=200*math.sin(k/10+m/72)+50*math.sin(k/7.2)

        #线段集:
        pu();pensize(4)
        goto(x*math.cos(m/38)-y*math.sin(m/38),x*math.sin(m/38)+y*math.cos(m/38))
        pencolor("#"+hex(0x100000+(m**4) % 0xEFFFFF)[2:]);pd()
        goto(x*math.cos(m/39)-y*math.sin(m/39),x*math.sin(m/39)+y*math.cos(m/39))

        #填充多边形:
        begin_fill()
        lt(.1)
        #fillcolor("#"+hex(0x100000+(m**4) % 0xEFFFFF)[2:])
        circle(7,steps=3)
        end_fill()
    #画图结束-----------------------------

    update() #<<=====更新画布=====
    k+=1 #<<=====变量递增=====
    ontimer(DrawLoop(), 50) #<<=====每隔n毫秒循环执行=====


ht() #隐藏乌龟
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====
