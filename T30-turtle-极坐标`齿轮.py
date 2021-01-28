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
    x=280*math.cos(v)+30*math.sin(8*v)
    y=280*math.sin(v)+30*math.cos(8*v)
    pencolor('red')
    setx(x)
    sety(y)
    v=v+PI/360
end_fill()
done()
