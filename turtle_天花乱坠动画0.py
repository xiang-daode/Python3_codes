# 在这里写上你的代码 :-)
from turtle import *
import math

w=0
def Draw():    
    global w    
    
    while(w<32768):
            clear()
            for q in range(-360,360+1,1):
                w+=0.01
                #指定区间逐一画图:                
                y=q*math.cos(w*q/360)
                x=q*math.sin(w*q/360)
                lt(0.1) #旋转(角度制)
                pu();goto(x,y);pd()
                begin_fill()  #开始填充
                rgb="#"+hex(0x800000+(int)(0x700000*math.sin(w/37)))[2:]
                fillcolor(rgb)  #填充色
                circle(10, steps=q%10+2)
                end_fill()    #结束填充
            update()   

tracer(False) #快速直接画    
ht() #隐藏乌龟
Draw()
