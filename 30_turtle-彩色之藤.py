from turtle import *
import math

# 彩色之藤:
pensize(6)
pu()
goto(-60,0)
pd()
for j in range(-90,95,1):
    r=0.5+0.5*math.cos(j/5.1)
    g=0.5+0.5*math.sin(j/3.7)
    b=0.5-0.5*math.cos(j/4.1)  
    pencolor(r,g,b)
    fd(30+j/5)                   
    lt(5*j % 120)
goto(0,-250)





