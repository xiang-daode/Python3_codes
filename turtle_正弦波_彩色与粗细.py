# 绘制波
import math
from turtle import *

color('black', 'blue')
ht(),up()
setpos(-315,0),pd()
pensize(4),pencolor(0,1,0)
v=0
while v<=630:
    x=v-315
    y=100*math.sin(x/50)
    goto(x,y)
    v=v+3
pensize(8),pencolor(0,0,1)
goto(-315,0)
