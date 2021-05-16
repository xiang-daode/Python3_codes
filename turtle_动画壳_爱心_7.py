# 在这里写上你的代码 :-)
from  turtle import *
import math
import sys


def DrawLoop():
    clear() #<<=====清空画布=====

    #画图开始:-----------------------------
    for m in range(-185,186,5):
        x=m*math.cos(m/18)
        y=m*math.sin(m/24)

        #填充多边形:
        begin_fill()
        lt(.1);goto(x,y)
        fillcolor("#"+hex(0x100000+(m**4) % 0xEFFFFF)[2:])
        circle(17,steps=3)
        end_fill()
    #画图结束-----------------------------

    update() #<<=====更新画布=====
    ontimer(DrawLoop(), 50) #<<=====每隔n毫秒循环执行=====


ht() #隐藏乌龟
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====
