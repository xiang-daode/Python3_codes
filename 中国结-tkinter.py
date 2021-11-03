# 从tkinter库中导入全部函数：
from tkinter import * #导入图像库
from math import * #导入数学库
import random as rnd #导入随机库
root = Tk() #建立根对象
canvas =Canvas( #绘图对象
width=800, #画布宽度
height=600, #画布高度
bg='#406080') #背景色
canvas.pack() #绘图对象生成
for g in range(1200):
    xc=400-150*cos(g/15)-100*sin(g/5) #计算坐标X
    yc=300-150*sin(g/15)-100*cos(g/5) #计算坐标Y
    canvas.create_oval( #画椭圆
    xc-10, #圆左上坐标：X
    yc-10, #圆左上坐标：Y
    xc+10, #圆右下坐标：X
    yc+10, #圆右下坐标：Y
    fill='#' + str(hex(rnd.randint(0x100000, 0xffffff)))[2:]) #随机填充色
root.mainloop() #保持画面
