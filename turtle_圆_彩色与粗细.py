import math
from turtle import *

pensize(4),pencolor(0,1,0)
ht(),pu()
for q in range(-314,+314,3):
    x=180*math.cos(q/100)
    y=180*math.sin(q/100)
    if q>=-314:
       goto(x,y),pd()
    goto(x,y)
