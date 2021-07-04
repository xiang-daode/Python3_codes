# Write your code here :-)
from turtle import *
from math import *
from time import *
#============
def rot(x,y,a,b,L1,L2):
    pu();goto(x,y);pd()
    lt(a);fd(L1);lt(b);fd(L2);lt(b*0.7);fd(L2/4)
#============
def main():
    for k in range(10):
        for g in range(-90,90,1):#正向
            a=g;b=1.5*g
            home();clear();
            rot(0,0,a,b,120,100)
            sleep(0.01)
            update()
        for g in range(90,-90,-1):#反向
            a=g;b=1.5*g
            home();clear();
            rot(0,0,a,b,120,100)
            sleep(0.01)
            update()
#===========
tracer(False);ht();pensize(8);pencolor(.3,0,0.3);main();


