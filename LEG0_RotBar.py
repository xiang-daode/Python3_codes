from turtle import *;  from math import *;  from time import *
def rot(x,y,a,L1):
    pu();goto(x,y);pd()
    lt(a);fd(L1);pu()
def main():
    for k in range(9999):
        for g in range(-60,60,1):
            clear()
            a=g;b=1.5*g
            pensize(8)
            home();rot(0,0,a,100)
            sleep(0.01); update()
#===========
tracer(False);ht();pencolor(.5,0,0);main()




