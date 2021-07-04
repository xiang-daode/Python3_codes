from turtle import *;from math import *;from time import *
def rot(x,y,a,b,L1,L2):
    pu();goto(x,y);pd()
    lt(a);fd(L1);lt(b);fd(L2);lt(b*7);fd(L2/4);pu();
def main():
    for k in range(2):
        for g in range(-60,60,1): #正向运动
            clear();
            a=g;b=1.5*g
            pensize(8);
            home();rot(0,0,a,b,100,80);
            home();rot(0,0,180-a,-b,100,80)
            sleep(0.01); update()
#===========
tracer(False);ht();pencolor(.5,0,0);main();




