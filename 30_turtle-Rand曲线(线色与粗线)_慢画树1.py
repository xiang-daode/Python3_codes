from turtle import *
import random as rnd

#  随机曲线:
setx(0);sety(-350)
lt(-90);pd()
#树杆:
for k in range(29):
    pencolor(rnd.random()/7,rnd.random(),rnd.random()/3)
    pensize(50-k)
    fd(-90/(k+1));lt(10*rnd.random()-5)
#树枝:
for k in range(9):
    setx(0);sety(-15*k);pd();
    for j in range(0,100,4):
        pensize(30-3*j/10)
        pencolor(rnd.random()/7,rnd.random(),rnd.random()/3)
        lt(180*rnd.random()-90)
        fd(50*rnd.random())
    pu()




