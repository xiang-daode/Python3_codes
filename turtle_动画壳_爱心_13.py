# 引入乌龟库,数学库:
from  turtle import *
import math

ht() #隐藏乌龟
pensize(4) #画笔粗细
pencolor(.75,0,.25)#画笔颜色

pu(); goto(0,0);pd()
for t in range(-188,188+4,4):
    x=t*math.cos(t/40)#X坐标计算
    y=t*math.sin(t/40)#Y坐标计算
    goto(x,y);






