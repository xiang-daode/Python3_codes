from turtle import * ;from math import *;from time import *;
#============
def rot(x,y,a,b,L1,L2):
    pu();goto(x,y+100);pd()
    lt(a);fd(L1);lt(b);fd(L2);lt(b*0.7);fd(L2/6); pu()
#============
def main():
    for k in range(500):
        for g in range(-60,60,1):
            a=g;b=1.5*g
            clear();
            #head & body:
            pensize(28);pencolor(.5,0.2,0.3)
            pu();goto(0,-20);pd();goto(0,100);pu()
            pu();goto(0,128);pd();goto(0,146);pu()
            #2 hands:
            pensize(12)
            home();rot(0,0,a,b,80,70)
            home();rot(0,0,180-a,90-b,80,70)
            #2 feet:
            pensize(18)
            home();rot(15,-120,-90+a*1.7,-b*1.5+20,120,100)
            home();rot(-15,-120,-90-a*1.7,+b*1.5-20,120,100)
            sleep(0.01);update()
#===========
tracer(False);ht();main();


