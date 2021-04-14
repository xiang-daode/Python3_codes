# 在这里写上你的代码 :-)
import math
import time
import tkinter as tk
import random as rnd
from tkinter import *
from turtle import *


# 定义tkinter画布:
root = tk.Tk()
root.title("[python+tkinter]动画设计器")
w = tk.Canvas(root, width=120, height=60, bg="#f0f0f0")
w.pack()

# 定义tkinter中心坐标:
x0, y0 = 600, 300

# 绘制标签:
lb = tk.Label(text="代码编写:  daode1212 (60后程序员), 2021-04-13", fg="#003399", bg="#FFEE88")
lb.config(bd=5, relief=SUNKEN)
lb.pack(side="bottom")


#turtle初始化:
reset()
setworldcoordinates(-600,-400,600,400)#设置坐标系
tracer(False)
ht()
pensize(2)


# 动画绘制函数-A:
def myDrawA(m):
    clear();tracer(False)
    for t in range(150):
        x1=t*math.cos(t/13)
        y1=t*math.sin(t/13)
        x2=x1*math.cos(m/17)-y1*math.sin(m/17)
        y2=x1*math.sin(m/17)+y1*math.cos(m/17)
        pencolor(math.exp(-t/100),0.5,math.exp(-t/100))
        goto(x2, y2)
        dot(16)
    update()
    m-=1
    while m>0:
      ontimer(myDrawA(m),50)

# 动画绘制函数-B:
def myDrawB(m):
    clear();tracer(False)
    for t in range(150):
        x1=t*math.cos(t/3)+180*math.cos(t/13)
        y1=t*math.sin(t/3)+180*math.cos(t/13)
        x2=x1*math.cos(m/17)-y1*math.sin(m/17)
        y2=x1*math.sin(m/17)+y1*math.cos(m/17)
        pencolor(0.5,math.exp(-t/100),math.exp(-t/100))
        goto(x2, y2)
        dot(5)
    update()
    m-=1
    while m>0:
      ontimer(myDrawB(m),50)

# 动画绘制函数-C:
def myDrawC(m):
    clear();tracer(False)
    for t in range(150):
        x1=120*math.cos(t/17)
        y1=120*math.sin(t/17)
        x2=x1*math.cos(m/37)-y1*math.sin(m/17)
        y2=x1*math.sin(m/37)+y1*math.cos(m/17)
        pencolor(0.5,math.exp(-t/100),math.exp(-t/100))
        goto(x2, y2)
        dot(25)
    update()
    m-=1
    while m>0:
      ontimer(myDrawC(m),50)

# 动画绘制函数-D:
def myDrawD(m):
    clear();tracer(False)
    for t in range(150):
        x1=t*math.cos(t/12)+136*math.cos(t/7)
        y1=t*math.sin(t/12)+136*math.sin(t/7)
        x2=x1*math.cos(m/17)-y1*math.sin(m/17)
        y2=x1*math.sin(m/17)+y1*math.cos(m/17)
        pencolor(0.5,math.exp(-t/100),math.exp(-t/100))
        goto(x2, y2)
        dot(5)
    update()
    m-=1
    while m>0:
      ontimer(myDrawD(m),50)


# 布局各按钮:
tk.Button(
    root, text="[按钮A:变形与旋转]", command=(lambda: myDrawA(900)), compound="center"
).pack(side="left")
tk.Button(
    root, text="[按钮B:变形与旋转]", command=(lambda: myDrawB(900)), compound="center"
).pack(side="left")
tk.Button(
    root, text="[按钮C:变形与旋转]", command=(lambda: myDrawC(900)), compound="center"
).pack(side="left")
tk.Button(
    root, text="[按钮D:变形与旋转]", command=(lambda: myDrawD(900)), compound="center"
).pack(side="left")

# 启动主程序:
root.mainloop()
