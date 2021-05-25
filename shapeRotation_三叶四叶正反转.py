from  turtle import *
from  tkinter import  *
from  math import *

screensize(1080, 900, "#666")
k=1 #<<====全局变量======
R=180 #
r=130 #


def myFun():
    s = Shape("compound")
    #------------------
    poly1 = []
    for q in range(-180,189,9):
        x=int(R*cos(pi*q/180+k)*cos(pi*q/90))
        y=int(R*sin(pi*q/180+k)*cos(pi*q/90))
        poly1.append([x,y])
    s.addcomponent(poly1, "red", "red")
    #------------------
    poly2 = []
    for q in range(-180,189,9):
        x=int(r*cos(pi*q/180-k)*cos(pi*q/60))
        y=int(r*sin(pi*q/180-k)*cos(pi*q/60))
        poly2.append([x,y])
    s.addcomponent(poly2, "blue", "blue")
    #-----------------
    register_shape("myshape", s)
    shape("myshape")

def DrawLoop():
    global k #<<====全局变量======
    while(k<32768):
        clear() #<<=====清空画布=====
        myFun() #<<=====调用画图函数=======
        update() #<<=====更新画布=====
        k+=0.001 #<<=====变量递增=====


#==========================
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====



