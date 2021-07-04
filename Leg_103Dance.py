# Write your code here :-)
from turtle import *
from math import *
from time import *

#============
def rot(x,y,a,b,L1,L2):
    pu();goto(x,y+100);
    pd()
    lt(a);fd(L1);lt(b);fd(L2);lt(b*0.7);fd(L2/4)
    pu()


#============
def main():
    for k in range(10):
        for g in range(-30,30,1):
            a=g;b=1.5*g
            clear();
            #body:
            pensize(28);pencolor(.5,0.2,0.3)
            pu();goto(0,-20);pd();goto(0,100);pu()
            pu();goto(0,128);pd();goto(0,146);pu()
            
            #hand:
            pensize(8)
            home();rot(0,0,a,b,80,70)
            home();rot(0,0,180-a,180-b,80,70)
            
            #foot:
            pensize(12)
            home();rot(-15,-120,-90+a*1.2,-b*1.5-20,120,100)
            home();rot(15,-120,-90-a*1.2,b*1.5+20,120,100)            

            sleep(0.01)
            update()       
            
#===========
tracer(False)
ht();

main();

    