# 在这里写上你的代码 :-)
from  turtle import *;  import math;  import sys;
sys.setrecursionlimit(900000)#修改最大递归层数到900000
k=1 #<<====全局变量======
def DrawLoop():
    global k #<<====全局变量======
    clear() #<<=====清空画布=====
    #画图开始:-----------------------------
    x=300*math.cos(k/2345)
    y=250*math.sin(k/1234)
    goto(x,y)
    color("black", "red")
    begin_fill()
    circle(50)
    end_fill()
    #画图结束-----------------------------

    update() #<<=====更新画布=====
    k+=1 #<<=====变量递增=====
    ontimer(DrawLoop(), 50) #<<=====每隔n毫秒循环执行=====
ht() #隐藏乌龟
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====
