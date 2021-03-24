# 绘制波
import math
from turtle import *
color('black', 'blue')

v=0

up()
setpos(300,0)
pd()
while v<600:
    x=v-300.0
    y=100*math.sin(x/30)+50*math.cos(x/10)
    setx(x)
    sety(y)
    v=v+3
done()
