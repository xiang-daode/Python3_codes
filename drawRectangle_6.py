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

ht();tracer(False)
for x in range(-400,450,50):
    h=randint(100,400)
    r=random();g=random();b=random();
    drawRect(x,-200,h,45,r,g,b)
