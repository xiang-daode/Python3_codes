from turtle import * ; from math import * ; from time import *
def rot(x,y,a,b,L1,L2): #运动关节
    pu();goto(x,y);pd()
    lt(a);fd(L1);lt(b);fd(L2);lt(b*7);fd(L2/4);pu()
def main():  #主函数
    for k in range(9999):
        for g in range(-60,60,1):
            clear()
            a=g;b=1.5*g #旋转角度
            pensize(8)#上肢粗细
            home();rot(18,0,a,b,100,80) #手1
            home();rot(-18,0,150-a,-b,100,80)#手2
            pensize(18) #下肢粗细
            home();rot(19,-120,-90+a/3,b/7,120,100) #脚1
            home();rot(-19,-120,-90-a/3,-b/7,120,100) #脚2
            pensize(32);pu();goto(0,30);pd();goto(g%20-10,40);pu() #头
            pensize(38);pu();goto(0,0);pd();goto(0,-120);pu() #体,躯干
            sleep(0.01); update()
#===========
tracer(False);ht();pencolor(.5,0,0);main()




