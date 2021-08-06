# draw Rectangle in Python Turtle
from turtle import *

#坐标(x,y), 高度h,宽度w,红r,绿g,蓝b
def drawRect(x,y,h,w,r,g,b):
    color(r,g,b);pu()
    goto(x,y);pd()
    begin_fill()
    for _ in range(4):
      if _% 2 == 0:
        forward(w)
        left(90)
      else:
        forward(h)
        left(90)
    end_fill()

drawRect(-200,-200,223,95,1,0,0)
drawRect(-100,-200,273,95,0,1,0)
drawRect(0,-200,293,95,0,.4,0)
drawRect(100,-200,273,95,0,1,1)
drawRect(200,-200,253,95,.3,1,0)
