import math
from turtle import *


#draw a circle:
color('red', 'yellow')
begin_fill()
while True:
    forward(5)
    left(3)
    if abs(pos()) < 1:
        break
end_fill()


#draw a poly_8:
color('blue', 'pink')
begin_fill()
while True:
    forward(90)
    left(360/8)
    if abs(pos()) < 1:
        break
end_fill()


#draw a star_5:
color('green', 'red')
begin_fill()
while True:
    forward(200)
    left(180-180/5)
    if abs(pos()) < 1:
        break
end_fill()



#draw a H-line:
color('green', 'red')
x=-300
pu()
goto(x,0)
pd()
while x<300:
    goto(x,0)
    x=x+5

#draw a V-line:
color('green', 'red')
y=-300
pu()
goto(0,y)
pd()
while y<300:
    goto(0,y)
    y=y+5



#draw a sin:
color('green', 'red')
x=-400
pu();width(5)
goto(x,0)
pd()
while x<400:
    y=200*math.sin((x+400)/50)
    goto(x,y)
    x=x+5


#draw a 傅里叶级数:
color('black', 'red')
x=-500
pu()
goto(x,0)
pd()
while x<500:
    y=200*math.sin((x+400)/50)+100*math.sin(3*(x+400)/50)+50*math.sin(5*(x+400)/50)+25*math.sin(7*(x+400)/50)
    goto(x,y)
    x=x+5



#draw a 双螺线:
color('red', 'yellow')
begin_fill()
x=-200
pu()
goto(x,0)
pd();width(8)
while x<200:    
    a= 180*math.sin(x/500.0)
    left(a)
    forward(40)
    x+=5;



done() #<<<========    The End =========

