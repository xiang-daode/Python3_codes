from turtle import *

#太阳花(3--N角星):
pensize(6)
pencolor(0,0,1)
fillcolor(1,0,1)
begin_fill()
n=5
for j in range(0,360,360//n):
    fd(250)
    lt(180-180//n)
end_fill()




