import math
from turtle import *

x0=300;y0=240
#两个多边形的数据加入复合体中,各点坐标可从画图软件中记录:
s = Shape("compound")
poly1 = ((181-y0,376-x0),(375-y0,566-x0),(375-y0,18-x0),(183-y0,194-x0)) #(y,x)
s.addcomponent(poly1, "red", "blue")
poly2 = ((111-y0,286-x0),(224-y0,400-x0),(225-y0,343-x0),(337-y0,343-x0),(332-y0,230-x0),(226-y0,232-x0),(223-y0,174-x0))
s.addcomponent(poly2, "blue", "red")

#接下来将 Shape 对象添加到 Screen 对象的形状列表并绘制它:
register_shape("myshape", s)

shape("myshape") #绘制


