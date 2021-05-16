# 引入乌龟库,数学库:
from  turtle import *
import math

def DrawLoop():
    clear() #<<=====清空画布=====
    #画图开始:-----------------------------
    for m in range(-180,181,3):
        x=m*math.cos(m/38)#坐标计算
        y=m*math.sin(m/38)#坐标计算

        begin_fill()#填充多边形
        lt(.1);goto(x,y) #旋转与定位
        fillcolor("#"+hex(0x100000+(m**4) % 0xEFFFFF)[2:]) #生成彩色
        circle(17,steps=3) #以指定半径,边数画圆(或正多边形)
        end_fill()#结束填充
    #画图结束-----------------------------
    update() #<<=====更新画布=====
    ontimer(DrawLoop(), 50) #<<=====每隔n毫秒循环执行DrawLoop()=====

ht() #隐藏乌龟
tracer(False) #False:快速直接画
DrawLoop() #<<=====执行[开始]=====
