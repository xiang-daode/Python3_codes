import math
from turtle import *

pensize(4),pencolor(0,1,0)
ht(),pu()
for q in range(-314,+314,1):
    x=180*math.cos(q/30)*math.cos(q/5)
    y=180*math.sin(q/30)*math.cos(q/5)
    pencolor(x%1,q%1,y%1)
    if q>=-314:
       goto(x,y),pd()
    goto(x,y)
