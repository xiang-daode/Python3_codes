# 绘制波
import math
from turtle import *

color('black', 'blue')

up()
setpos(315,0)
pd()

v=0
while v<630:
    x=v-315
    y=100*math.sin(x/50)
    setx(x)
    sety(y)
    v=v+3
done()
