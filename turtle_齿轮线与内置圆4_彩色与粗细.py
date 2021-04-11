import math
from turtle import *

pensize(4),pencolor(0,1,0)
ht(),pu()
for q in range(0,628+3,3):
    x=(150 if (q % 30 >15) else 130)*math.cos(q/100)
    y=(150 if (q % 30 >15) else 130)*math.sin(q/100)
    pencolor((x%30)/30,(q%30)/30,(y%30)/30)
    if q>=0:
       goto(x,y),pd()
    goto(x,y)
pu(),goto(0,-120),pd()
circle(120)
