from turtle import *
from math import *
import time
w=0
tracer(False) #快速直接画
ht() #隐藏乌龟
def main():
    global w;clear();home()
    pu();goto(0,0) #<-------手1-------
    x=30*sin(w);y=180-30*sin(w)
    pd();lt(x);fd(100)
    lt(1.25*x);fd(100);pu();
    goto(0,0);pd();lt(y);fd(100)#<------手2--------
    rt(-1.25*x);fd(100);pu();
    w +=.1
    update();time.sleep(.001)
    ontimer(main(),1)
pensize(8)
main()

