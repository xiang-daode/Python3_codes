#
from turtle import * ;from math import *;from time import *;
#============
def rotR(x,y,a,b,L1,L2):
    pu();goto(x,y);pd()
    a+=b;
    lt(180-a);fd(L1);lt(-1.5*a);fd(L2);lt(-a*2.0);fd(L2/3);pu()
def rotL(x,y,a,b,L1,L2):
    pu();goto(x,y);pd()
    a+=b;
    lt(a);fd(L1);lt(1.5*a);fd(L2);lt(a*2.0);fd(L2/3);pu()

#============
def main():
    for h in range(9999):
        my=160-30*(h%20)
        #home();
        for g in range(-15,15,1):
            a=g;b=a+15;
            clear();pencolor(0,0,0.3)

            #3 feet for left :
            pensize(4)
            home();rotL(20,-10+my,a,10,40,40)
            home();rotL(20,-0+my,a,20,40,40)
            home();rotL(20,10+my,a,30,40,40)

            #3 feet for right :
            pensize(4)
            home();rotR(-20,-10+my,a,10,40,40)
            home();rotR(-20,0+my,a,20,40,40)
            home();rotR(-20,10+my,a,30,40,40)

            # head & body:
            pu();goto(0,my-10);pencolor(0,.3,0);pensize(40);pd();goto(0,my+10);pu() #body-1
            pu();goto(0,my+50);pencolor(.3,0,0);pensize(40);pd();goto(0,my+90);pu() #body-2
            pu();goto(0,my-45);pencolor(0,0,.3);pensize(20);pd();goto(0,my-40);pu()  #head

            sleep(0.01);update()
#===========
tracer(False);ht();
main();


