import math
from turtle import *

color('black', 'blue')
begin_fill()
v=0
ht()
PI=3.1415928
up()
setpos(280,30)
pd()
while v<2*PI:
    x=280*math.cos(9*v)+30*math.sin(15*v)
    y=280*math.sin(6*v)+30*math.cos(12*v)
    setx(x)
    sety(y)
    v=v+PI/180
end_fill()
done()
