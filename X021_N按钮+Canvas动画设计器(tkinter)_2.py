# 在这里写上你的代码 :-)
import math
import time
import tkinter as tk
import random as rnd
from tkinter import *

# 定义画布:
root = tk.Tk()
root.title("[python+tkinter]动画设计器")
w = tk.Canvas(root, width=1200, height=600, bg="#000")
w.pack()

# 定义中心坐标:
x0, y0 = 600, 300

# 绘制标签:
lb = tk.Label(text="代码编写:  daode1212 (60后程序员), 2021-04-13", fg="#003399", bg="#FFEE88")
lb.config(bd=5, relief=SUNKEN)
lb.pack(side="bottom")

# 动画绘制函数-A:
def myDrawA():
    r = 250
    for g in range(-200, 200, 1):
        w.delete("all")
        u = 3600
        rgb = "#" + str(hex(rnd.randint(0x888888, 0xFFFFFF)))[2:]  # 生成随机颜色
        while u > 0:
            x1, y1 = (
                r * math.cos((u - 2) / 34) * math.cos(g / 234),
                r * math.sin((u - 2) / 48) * math.cos(g / 134),
            )
            x2, y2 = (
                r * math.cos((u + 2) / 34) * math.cos(g / 134),
                r * math.sin((u + 2) / 48) * math.cos(g / 234),
            )
            x3 = x1 * math.cos(g / 45) - y1 * math.sin(g / 45)
            y3 = x1 * math.sin(g / 45) + y1 * math.cos(g / 45)
            x4 = x2 * math.cos(g / 45) - y2 * math.sin(g / 45)
            y4 = x2 * math.sin(g / 45) + y2 * math.cos(g / 45)
            w.create_line(x0 + x4, y0 + y4, x0 + x3, y0 + y3, fill=rgb, width=8)
            u -= 5
        w.update()
        time.sleep(0.001)


# 动画绘制函数-B:
def myDrawB():
    r = 250
    for g in range(-200, 200, 1):
        w.delete("all")
        u = 3600
        rgb = "#" + str(hex(rnd.randint(0x888888, 0xFFFFFF)))[2:]  # 生成随机颜色
        while u > 0:
            x1, y1 = r * math.cos((g + u + 3) / 79), r * math.sin((g - u + 3) / 79)
            x2, y2 = r * math.cos((g + u) / 79), r * math.sin((g - u) / 79)
            x3 = x1 * math.cos(g / 45) - y1 * math.sin(g / 45)
            y3 = x1 * math.sin(g / 45) + y1 * math.cos(g / 45)
            x4 = x2 * math.cos(g / 45) - y2 * math.sin(g / 45)
            y4 = x2 * math.sin(g / 45) + y2 * math.cos(g / 45)
            rgb = "#" + str(hex(0x100000 + int(x3 * y4 * g) % 0xEFFFFF))[2:]  # 生成随机颜色
            w.create_line(x0 + x4, y0 + y4, x0 + x3, y0 + y3, fill=rgb, width=8)
            u -= 5
        w.update()
        time.sleep(0.001)


# 动画绘制函数-C:
def myDrawC():
    r = 250
    for g in range(-200, 200, 1):
        w.delete("all")
        u = 3600
        rgb = "#" + str(hex(rnd.randint(0x888888, 0xFFFFFF)))[2:]  # 生成随机颜色
        while u > 0:
            x1, y1 = r * math.cos((g + u + 0.3) / 34), r * math.sin((g - u + 0.3) / 48)
            x2, y2 = r * math.cos((g + u) / 34), r * math.sin((g - u) / 48)
            x3 = x1 * math.cos(g / 45) - y1 * math.sin(g / 45)
            y3 = x1 * math.sin(g / 45) + y1 * math.cos(g / 45)
            x4 = x2 * math.cos(g / 65) - y2 * math.sin(g / 75)
            y4 = x2 * math.sin(g / 65) + y2 * math.cos(g / 75)
            rgb = "#" + str(hex(0x100000 + int(x3 * y4 * g) % 0xEFFFFF))[2:]  # 生成随机颜色
            w.create_line(x0 + x4, y0 + y4, x0 + x3, y0 + y3, fill=rgb, width=8)
            u -= 5
        w.update()
        time.sleep(0.001)


# 动画绘制函数-D:
def myDrawD():
    r = 250
    for g in range(-200, 200, 1):
        w.delete("all")
        u = 3600
        while u > 0:
            x1, y1 = r * math.cos((g + u - 3) / 74), r * math.sin((g - u + 3) / 152)
            x2, y2 = r * math.cos((g + u) / 74), r * math.sin((g - u) / 152)
            x3 = x1 * math.cos(g / 45) - y1 * math.sin(g / 45)
            y3 = x1 * math.sin(g / 45) + y1 * math.cos(g / 45)
            x4 = x2 * math.cos(g / 45) - y2 * math.sin(g / 45)
            y4 = x2 * math.sin(g / 45) + y2 * math.cos(g / 45)
            rgb = "#" + str(hex(0x100000 + int(x3 * y4 * g) % 0xEFFFFF))[2:]  # 生成随机颜色
            w.create_line(x0 + x4, y0 + y4, x0 + x3, y0 + y3, fill=rgb, width=8)
            u -= 5
        w.update()
        time.sleep(0.001)


# 布局各按钮:
tk.Button(
    root, text="[按钮A:变形与旋转]", command=(lambda: myDrawA()), compound="center"
).pack(side="left")
tk.Button(
    root, text="[按钮B:变形与旋转]", command=(lambda: myDrawB()), compound="center"
).pack(side="left")
tk.Button(
    root, text="[按钮C:变形与旋转]", command=(lambda: myDrawC()), compound="center"
).pack(side="left")
tk.Button(
    root, text="[按钮D:变形与旋转]", command=(lambda: myDrawD()), compound="center"
).pack(side="left")

# 启动主程序:
root.mainloop()
