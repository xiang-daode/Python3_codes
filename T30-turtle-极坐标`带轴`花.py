import math
from turtle import *
speed(0)
color('blue', 'yellow')
v=0
ht()
PI=3.1415928
up()
setpos(200,60)
pd()
width(4)
while v<2*PI:
    x=200*math.cos(v)+60*math.sin(v*7)
    y=200*math.sin(v)+60*math.cos(v*7)
    setx(x)
    sety(y)
    v=v+PI/180

width(8)

color('green', 'blue')
up();setpos(-300,0)
pd();forward(600)

color('red', 'blue')
up();setpos(0,300)
left(90)
pd();forward(-600)


done()
