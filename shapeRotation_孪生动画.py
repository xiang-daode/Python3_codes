from  turtle import *
from  tkinter import  *
from  math import *

screensize(1080, 900, "#666")
u,v,w=0,0,0 #<<====全局变量======
R=180 #

def myFun():
    s = Shape("compound")
    #------------------
    poly1 = []
    for q in range(-180,183,1):
        x=int(R*cos(pi*q/180+v)+99*sin(u*pi*q/90)+77*cos(v*pi*q/30))
        y=int(R*sin(pi*q/180+v)+99*cos(u*pi*q/90)+77*sin(v*pi*q/30))
        poly1.append([x,y-250])
    rgb="#"+hex((0x100000+w*7)% 0xFFFFFF)[2:]
    clr="#"+hex((0x100000+w*3)% 0xFFFFFF)[2:]
    s.addcomponent(poly1, rgb, clr)
    #-----------------
    poly2 = []
    for q in range(-180,183,1):
        x=int(R*cos(pi*q/180+v)+99*sin(u*pi*q/90)+77*cos(v*pi*q/30))
        y=int(R*sin(pi*q/180+v)+99*cos(u*pi*q/90)+77*sin(v*pi*q/30))
        poly2.append([x,-y+250])
    rgb="#"+hex((0x100000+w*3)% 0xFFFFFF)[2:]
    clr="#"+hex((0x100000+w*9)% 0xFFFFFF)[2:]
    s.addcomponent(poly2, rgb, clr)
    #-----------------

    register_shape("myshape", s)
    shape("myshape")

def DrawLoop():
    global u,v,w #<<====全局变量======
    while(w<0xFFFFFF):
        clear() #<<=====清空画布=====
        myFun() #<<=====调用画图函数=======
        update() #<<=====更新画布=====
        u=cos(w/1379) #<<=====变量递增=====
        v=sin(w/1468) #<<=====变量递增=====
        w+=1 #<<=====变量递增=====
    u,v,w=0,0,0
    DrawLoop()

#==========================
tracer(False) #快速直接画
DrawLoop() #<<=====执行[开始]=====



