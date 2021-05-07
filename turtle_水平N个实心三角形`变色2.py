# 多彩三角形:
from turtle import *

def Trgl(x,y): #自定义函数:画彩色三角形
    pu(); goto(x,y); pd(); lt(45) #提笔,去某点,下笔, 旋转(角度制)
    fillcolor("#"+hex(0x100000+(x**8) % 0xEFFFFF)[2:])  #填充色
    begin_fill()  #开始填充
    circle(20, steps=3) #画多边形,半径?几边?
    end_fill()    #结束填充

ht() #隐藏乌龟
color("red")  #画笔颜色为红色
tracer(False) #快速直接画

#指定区间(范围)逐一画图:
for x in range(-350,350,10):
    Trgl(x,x) #执行自定义函数


