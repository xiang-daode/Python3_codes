from turtle import *
from math import *
import time
w=0 #计步器变量
tracer(False) #快速直接画
ht() #隐藏乌龟
def main(): #自制函数
    global w;clear();home()
    pu();goto(0,0)
    g=30*sin(w)
    pd();lt(g);fd(100)
    lt(1.5*g);fd(100);pu();
    w+=.1
    update();time.sleep(.01)
    ontimer(main(),50)
pensize(8)
main()

