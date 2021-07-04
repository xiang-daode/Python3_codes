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
    for m in range(0,201,2):
        #坐标计算:
        x=2*m + (k % 800)-600
        y=0.2*m*math.sin(m/13+k/7)

        #线段集:
        pu();pensize(8)
        goto(x,y-m/40)
        clr="#"+hex(0x100000+(m**2) % 0xEFFFFF)[2:]
        pencolor(clr);pd()
        goto(x,y+m/40)

        if(m==200):
                #clr="#888";pencolor(clr);
                goto(x+24,y+12*math.sin(m/13+k/7));goto(x,y);goto(x+24,y-6*math.sin(m/13+k/7));goto(x,y);goto(x+12,y);
                #填充多边形:
                goto(x+4,y+6);
                begin_fill()
                #lt(m/50)
                fillcolor("#fff");pencolor("#484");
                circle(4,steps=12)
                end_fill()


    #画图结束-----------------------------

    update() #<<=====更新画布=====
    k+=1 #<<=====变量递增=====
    ontimer(DrawLoop(), 50) #<<=====每隔n毫秒循环执行=====


ht() #隐藏乌龟
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====
