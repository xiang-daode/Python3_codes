from turtle import *
import random as rnd

#  随机曲线:
for k in range(9):
    setx(0);sety(0);pd();
    for j in range(0,100,4):
        pensize(30-3*j/10)
        pencolor(rnd.random()/7,rnd.random(),rnd.random()/3)
        lt(180*rnd.random()-90)
        fd(50*rnd.random())
    pu()




