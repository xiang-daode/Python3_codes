from turtle import *
import math
##############################################
d=300
n=7
##############################################
N=0
color('red', 'yellow')
begin_fill()
pu();goto(-d/2,100);pd()
while N<=n:
    forward(d)
    left(180-180/n)
    N=N+1
    if abs(pos()) < 1:
        break
end_fill()
pu()


color('blue', 'green')
begin_fill()
N=0
goto(d/2,-100);pd()
while N<n:
    forward(d/8)
    left(360/n)
    N=N+1
    if abs(pos()) < 1:
        break
end_fill()


color('red', 'pink')
begin_fill()
N=-185
pd()
while N<185:
    q=3.1416*N/180
    x=-400+0.5*d*math.sin(q)+50*math.cos(q*n)
    y=0.5*d*math.cos(q)+50*math.sin(q*n)
    goto(x,y)
    N=N+1
end_fill()


color('green', 'pink')
begin_fill()
N=-185
pd()
while N<185:
    q=3.1416*N/180
    x=400+0.5*d*math.sin(q)-20*math.cos(q*n)
    y=0.5*d*math.cos(q)-20*math.sin(q*n)
    goto(x,y)
    N=N+1
end_fill()


done()
