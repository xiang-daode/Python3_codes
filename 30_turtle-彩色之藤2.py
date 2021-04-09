from turtle import *
import math

# 彩色之藤:
pensize(6)
pu()
goto(-320,220)
pd()
for j in range(-90,360,1):
    r=0.5+0.5*math.cos(j/5)
    g=0.5+0.5*math.sin(j/4)
    b=0.5-0.5*math.cos(j/3)  
    pencolor(r,g,b)
    fd(3+j%20)                   
    lt(60*math.cos(j/37))






