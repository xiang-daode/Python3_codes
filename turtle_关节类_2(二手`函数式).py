from turtle import *
from math import *
import time

w=0
tracer(False) #快速直接画
ht() #隐藏乌龟

def LegA(x,y,w):
    A1=30*sin(w);A2=45*sin(w)
    pu();goto(x,y)
    pd();lt(A1);fd(100)
    lt(A2);fd(100);pu();

def LegB(x,y,w):
    A1=180-30*sin(w);A2=45*sin(w)
    pu();goto(x,y)
    pd();lt(A1);fd(100)
    lt(A2);fd(100);pu();

def LegC(x,y,w):
    A1=90-30*sin(w);A2=45*sin(w)
    pu();goto(x,y)
    pd();lt(A1);fd(100)
    lt(A2);fd(100);pu();

def LegD(x,y,w):
    A1=90+30*sin(w);A2=45*sin(w)
    pu();goto(x,y)
    pd();lt(A1);fd(100)
    lt(A2);fd(100);pu();

def main():
    global w;clear();home()
    LegA(20,0,w);
    LegB(-20,0,w)
    LegC(20,-150,w)
    LegD(-20,-150,w)
    w +=.01
    update();time.sleep(.001)
    ontimer(main(),1)

pensize(8)
main()

