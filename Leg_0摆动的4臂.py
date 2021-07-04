# Write your code here :-)
from turtle import *
from math import *
from time import *
#============
def rot(x,y,a,b,L1,L2):
    pu();goto(x,y);pd();
    lt(a);fd(L1);lt(b);fd(L2);pu()
#============
def main():
    for k in range(100):
        for g in range(0,30,1): #正向运动
            home();clear();
            a=g;b=2*g
            home();rot(0,0,-a,-b,120,100);
            home();rot(0,-140,-125+a,+b,120,100);
            home();rot(0,0,180+a,+b,120,100);
            home();rot(0,-140,-55-a,-b,120,100);
            sleep(0.01); update()
        for g in range(30,0,-1):#逆向运动
            home();clear();
            a=g;b=2*g
            home();rot(0,0,a,b,120,100);
            home();rot(0,-140,-125-a,-b,120,100);
            home();rot(0,0,180-a,-b,120,100);
            home();rot(0,-140,-55+a,+b,120,100);
            sleep(0.01); update()
#===========
tracer(False);ht();pensize(8);pencolor(.5,0,0)
main();


