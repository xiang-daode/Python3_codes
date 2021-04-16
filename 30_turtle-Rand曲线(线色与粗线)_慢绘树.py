from turtle import *
import random as rnd

#  随机曲线:
for k in range(5):
    setx(0);sety(0);pd()
    for j in range(0,100,2):
        pensize(10-j/10)
        pencolor(rnd.random()/7,rnd.random(),rnd.random()/5)
        lt(60*rnd.random()-30)
        fd(8*rnd.randint(-5,5))
    pu()
setx(0);sety(0);pd()
pensize(13)
goto(0,-250)



