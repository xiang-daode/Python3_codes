from  turtle import *
import math
import sys
k=1 #<<====全局变量======
def DrawLoop():
    global k #<<====全局变量======
    clear() #<<=====清空画布=====
    for m in range(-185,186,5):
        x=m*math.cos(m/18)
        y=m*math.sin(m/24)
        #填充多边形:
        begin_fill()
        lt(.1);goto(x,y)
        fillcolor("#"+hex(0x100000+(m**4) % 0xEFFFFF)[2:])
        circle(k%17,steps=3+k%9)
        end_fill()
    update() #<<=====更新画布=====
    k+=1 #<<=====变量递增=====
    ontimer(DrawLoop(), 50) #<<=====每隔n毫秒循环执行=====
ht() #隐藏乌龟
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====
