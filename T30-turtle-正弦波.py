import math
from turtle import *

color('black', 'blue')

v=0
ht()

up()
setpos(300,0)
pd()
while v<600:
    x=v-300
    y=240*math.sin(v/45)+60*math.cos(v/25)
    setx(x)
    sety(y)
    v=v+3
done()
