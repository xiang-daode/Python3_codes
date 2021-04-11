import math
from turtle import *

pensize(4),pencolor(0,1,0)
ht(),pu()
for q in range(0,628+3,3):
    x=(150-q % 30)*math.cos(q/100)
    y=(150-q % 30)*math.sin(q/100)
    pencolor(x%1,0.5,y%1)
    if q>=0:
       goto(x,y),pd()
    goto(x,y)
