from  turtle import *
from  tkinter import  *
from  math import *

screensize(1080, 900, "#666")
k,h,m=0,0,0 #<<====全局变量======
R=180 #

def myFun():
    s = Shape("compound")
    #------------------
    poly1 = []
    for q in range(-180,189,9):
        x=int(R*cos(pi*q/180+k)+99*sin(k*pi*q/90)+15*cos(h*pi*q/15))
        y=int(R*sin(pi*q/180+k)+99*cos(k*pi*q/90)+15*sin(h*pi*q/15))
        poly1.append([x,y])
    rgb="#"+hex((m+0x123456)% 0xEFFFFF)[2:]
    clr="#"+hex((m+0x654321)% 0xEFFFFF)[2:]
    s.addcomponent(poly1, rgb, clr)
    #-----------------
    register_shape("myshape", s)
    shape("myshape")

def DrawLoop():
    global k,h,m #<<====全局变量======
    while(k<32768):
        clear() #<<=====清空画布=====
        myFun() #<<=====调用画图函数=======
        update() #<<=====更新画布=====
        k+=0.0001357 #<<=====变量递增=====
        h+=0.0002468 #<<=====变量递增=====
        m+=1 #<<=====变量递增=====

#==========================
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====



