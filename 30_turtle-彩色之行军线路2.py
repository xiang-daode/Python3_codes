from turtle import *
import math

# 彩色之藤:
pensize(6)
pu()
goto(-120,270) #-375...375,-275..275
pd()
for j in range(-90,180,1):
    r=0.5+0.5*math.cos(j/5)
    g=0.5+0.5*math.sin(j/4)
    b=0.5-0.5*math.cos(j/3)
    pencolor(r,g,b)
    fd(5)
    lt(45*(math.cos(j/7)*math.sin(j/5)))






