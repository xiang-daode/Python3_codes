import math
from turtle import *

color('black', 'blue')

v=0
ht()

up()
setpos(-300,0)
pd()
while v<600:
    x=v-300
    y=200*math.sin(v/75)+60*math.cos(v/10)
    setx(x)
    sety(y)
    v=v+3

width(8)

color('green', 'blue')
up();setpos(-300,0)
pd();forward(600)

color('red', 'blue')
up();setpos(0,300)
left(90)
pd();forward(-600)
done()
