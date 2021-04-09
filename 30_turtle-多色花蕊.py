from turtle import *
import math


pensize(6)
pu()
goto(-100,0)
pd()
for j in range(-75,75,1):
    r=0.5+0.5*math.cos(j/3.1)
    g=0.5+0.5*math.sin(j/3.7)
    b=0.5-0.5*math.cos(j/4.1)
    pencolor(r,g,b)
    fd(30)
    lt(5*j % 90)






