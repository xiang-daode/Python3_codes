from turtle import *
import random as rnd

tracer(False)  # 快速(不用小乌龟)
ht()  # 隐藏小乌龟
#  随机曲线:
for k in range(35):
    setx(0);sety(0);pd()
    for j in range(0,100,2):
        pensize(10-j/10)
        pencolor(rnd.random()/5,rnd.random(),rnd.random()/7)
        lt(90*rnd.random()-45)
        fd(16*rnd.random())
    pu()

setx(0);sety(0);pd()
for j in range(0,100,2):
    pensize(10+j/3)
    pencolor(rnd.random()/5,rnd.random(),rnd.random()/7)
    lt(10*rnd.random()-5)
    fd(16*rnd.random())





