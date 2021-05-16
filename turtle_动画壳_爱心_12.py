# 引入乌龟库,数学库:
from  turtle import *
import math

ht() #隐藏乌龟
pensize(4) #画笔粗细
pencolor(.5,0,.5)#画笔颜色

pu(); goto(0,0);pd()
for t in range(-2*628,2*628,24):
    x=200*math.cos(t/60)#X坐标计算
    y=200*math.sin(t/42)#Y坐标计算
    goto(x,y);






