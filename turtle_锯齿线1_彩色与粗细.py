import math
from turtle import *

pensize(4),pencolor(0,1,0)
ht(),pu()
for q in range(0,300,1):
    x=150*math.cos(q/45)+20*math.sin(q/3)
    y=150*math.sin(q/45)+20*math.cos(q/3)
    pencolor(x%1,0.5,y%1)
    if q>=-314:
       goto(x,y),pd()
    goto(x,y)
