import math
from turtle import *

pensize(4),pencolor(0,1,0)
ht(),pu()
for q in range(0,200,1):
    x=q*math.cos(q/5)
    y=q*math.sin(q/5)
    pencolor(x%1,0.5,y%1)
    if q>=-314:
       goto(x,y),pd()
    goto(x,y)
