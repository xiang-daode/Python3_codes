# Write your code here :-)
from turtle import *
from math import *
from time import *

#============
def rot(x,y,a,b,L1,L2):
    pu();goto(x,y+100); pd();
    lt(a);fd(L1);lt(b);fd(L2);lt(b*0.7);fd(L2/4);pu();
#============
def main():
    for k in range(10):
        for g in range(-30,30,1):
            a=g;b=1.5*g
            clear();
            #body:
            pensize(38);pencolor(.5,0.2,0.8)
            pu();goto(0,-20);pd();goto(0,100);pu()
            #head:
            pensize(28);pencolor(.5,0.1,0.3)
            pu();goto(0,132);pd();goto(0,146);pu()

            #arm:
            pensize(8)
            home();rot(18,0,a,b,80,70)
            home();rot(-18,0,180-a,-b,80,70)
            #leg:
            pensize(18)
            pu();goto(12,-30);pd();goto(38,-200);goto(58,-200);
            pu();goto(-12,-30);pd();goto(-38,-200);goto(-58,-200);
            sleep(0.01)
            update()

#===========
tracer(False);ht();main();


