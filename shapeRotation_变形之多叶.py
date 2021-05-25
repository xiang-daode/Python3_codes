from  turtle import *
from  tkinter import  *
from  math import *

screensize(1080, 900, "#666")
k=1 #<<====全局变量======
R=180 #

def myFun():
    s = Shape("compound")
    #------------------
    poly1 = []
    for q in range(-180,189,9):
        x=int(R*cos(pi*q/180+k)*cos(k*pi*q/90))
        y=int(R*sin(pi*q/180+k)*cos(k*pi*q/90))
        poly1.append([x,y])
    s.addcomponent(poly1, "white", "red")
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



