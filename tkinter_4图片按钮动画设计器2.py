# 在这里写上你的代码 :-)
import math
import time
import tkinter as tk
import random as rnd
from tkinter import *

#定义画布:
root = tk.Tk()
root.title("[python+tkinter]动画设计器")
w = tk.Canvas(root, width=1200, height=600, bg="#000")
w.pack()

#定义中心坐标:
x0, y0 = 600, 300

#绘制标签:
lb = tk.Label(text="代码编写:  daode1212 (60后程序员), 2021-04-13", fg="#003399", bg="#FFEE88")
lb.config(bd=5,relief = SUNKEN)
lb.pack(side="bottom")

#动画绘制函数-A:
def myDrawA():
    r = 250
    for x in range(-200,200,3):
        w.delete("all")
        u=3600
        while u > 0:
            x1, y1 = x0, y0
            x2, y2 = x0 + r * math.cos(u / 45), y0 + r * math.sin(u / 60)
            w.create_line(x1+x, y1, x2+x, y2, fill="#FF4400", width=8)
            u -= 15
        w.update()
        time.sleep(0.001)

#动画绘制函数-B:
def myDrawB():
    r = 250
    for x in range(-200,200,3):
        w.delete("all")
        u=3600
        while u > 0:
            x1, y1 = x0, y0
            x2, y2 = x0 + r * math.cos(u / 45), y0 + r * math.sin(u / 60)
            w.create_line(x1, y1+x, x2, y2+x, fill="#FF4400", width=8)
            u -= 15
        w.update()
        time.sleep(0.001)

#动画绘制函数-C:
def myDrawC():
    r = 250
    for g in range(-200,200,3):
        w.delete("all")
        u=3600
        while u > 0:
            x1, y1 = x0, y0
            x2, y2 = r * math.cos(u / 45), r * math.sin(u / 60)
            x3=x0+x2*math.cos(g / 45)-y2*math.sin(g / 45)
            y3=y0+x2*math.sin(g / 45)+y2*math.cos(g / 45)
            w.create_line(x1, y1, x3, y3, fill="#FF4400", width=8)
            u -= 15
        w.update()
        time.sleep(0.001)

#动画绘制函数-D:
def myDrawD():
    r = 250
    for g in range(-200,200,1):
        w.delete("all")
        u=3600
        rgb ='#'+ str(hex(rnd.randint(0x888888, 0xFFFFFF)))[2:]  # 生成随机颜色
        while u > 0:
            x1, y1 = r * math.cos((g+u+3) / 64), r * math.sin((g-u+3) / 48)
            x2, y2 = r * math.cos((g+u) / 64), r * math.sin((g-u) / 48)
            x3=x1*math.cos(g / 45)-y1*math.sin(g / 45)
            y3=x1*math.sin(g / 45)+y1*math.cos(g / 45)
            x4=x2*math.cos(g / 45)-y2*math.sin(g / 45)
            y4=x2*math.sin(g / 45)+y2*math.cos(g / 45)
            w.create_line(x0+x4, y0+y4, x0+x3, y0+y3, fill=rgb, width=8)
            u -= 5
        w.update()
        time.sleep(0.001)

#布局各按钮:
tk.Button(root, text="[按钮A:左右移动]", command=(lambda: myDrawA()), compound="center").pack(
    side="left"
)
tk.Button(root, text="[按钮B:上下移动]", command=(lambda: myDrawB()), compound="center").pack(
    side="left"
)
tk.Button(root, text="[按钮C:二维旋转]", command=(lambda: myDrawC()), compound="center").pack(
    side="left"
)
tk.Button(root, text="[按钮D:变形与旋转]", command=(lambda: myDrawD()), compound="center").pack(
    side="left"
)

#启动主程序:
root.mainloop()
