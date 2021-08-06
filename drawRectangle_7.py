# draw Rectangle in Python Turtle
from turtle import *
from random import *

#坐标(x,y), 高度h,宽度w,红r,绿g,蓝b
def drawRect(x,y,h,w,r,g,b):
    pu();color(r,g,b);pencolor(0.5*r,0.5*g,0.5*b);pensize(2)
    goto(x,y);pd()
    begin_fill()
    for k in range(4):
      if k % 2 == 0:
        forward(w)
        left(90)
      else:
        forward(h)
        left(90)
    end_fill()

#将列表数据以条形统计图显示:
data=[175,225,360,148,262,150,247,320,261,98,189,75,157]
ht();tracer(False)
n=len(data);ww=600 #ww:条形图总宽度
for i in range(n):
    h=data[i]
    r=random();g=random();b=random();
    drawRect(ww*(i-n/2)/n,-200,h,ww/n,r,g,b)
