# 引入乌龟库,数学库:
from  turtle import *
import math

ht() #隐藏乌龟
pensize(133) #画笔粗细
pencolor(1,0,0)#画笔颜色

pu(); goto(0,0);pd()
for t in range(-188,188+4,4):
    x=t*math.cos(t/40)#X坐标计算
    y=t*math.sin(t/40)#Y坐标计算
    if(t<-59 or t>59): #跳过当中一段画
        goto(x,y);#画到(x,y)这一点






