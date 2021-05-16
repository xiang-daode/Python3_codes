# 引入乌龟库,数学库:
from  turtle import *
import math

ht() #隐藏乌龟
pensize(4) #画笔粗细
pencolor(1,0,1)#画笔颜色

pu(); goto(200,0);pd()
for t in range(0,628,24):
    x=200*math.cos(t/100)#X坐标计算
    y=200*math.sin(t/100)#Y坐标计算
    goto(x,y);






