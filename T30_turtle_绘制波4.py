# 绘制波
import math
from turtle import *

color('black', 'red')
x=-500
pu()
goto(x,0)
pd()
while x<500:
    y=300*math.sin((x+400)/50)+100*math.sin(3*(x+400)/50)+50*math.sin(5*(x+400)/50)+25*math.sin(7*(x+400)/50)
    goto(x,y)
    x=x+5
