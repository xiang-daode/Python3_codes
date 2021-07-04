#turtle动画蛙泳(代码撰写:项道德,2021-06-17):
from turtle import *
from math import *
from time import *
#============
def rot(x,y,a,b,L1,L2): #三段式运动机构
    home();pu();goto(x,y);pd();
    lt(a);fd(L1);lt(b);fd(L2);lt(b*3);fd(L2/4);pu()
def headBody(k):
    #body:
    pensize(48);pencolor(0,0,0.2)
    pu();goto(0,-10+k);pd();goto(0,-130+k);pu()
    #head:
    pensize(32);pencolor(0,0,0)
    pu();goto(0,30+k);pd();goto(0,40+k);pu()
#============
def main():
    for k in range(0,600,3):
        for g in range(-45,45,3): #单方向运动
            clear();#清空画布
            a=g;b=2*g;#二角度设置
            pensize(18);pencolor(.8,0,0)#上肢粗细与颜色
            rot(15,+k,-a,-b,100,100);#左手
            rot(-15,+k,180+a,+b,100,100);#右手
            pensize(28);pencolor(0,.2,0)#下肢粗细与颜色
            rot(-17,-140+k,-125+a/3,+b/4,120,120);#左脚
            rot(17,-140+k,-55-a/3,-b/4,120,120);#右脚
            headBody(k) #头与躯干
            sleep(0.01);update() #延时与更新画布
#===========
tracer(False);ht();pensize(8);pencolor(.5,0,0)
main();


