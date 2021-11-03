import math;import time;#import tkinter as tk
import random as rnd;from tkinter import *
#定义画布:
root = Tk();root.title("[python+tkinter]动画设计器")
w = Canvas(root, width=1200, height=600, bg="#FFF");w.pack()
x0, y0 = 600, 300 #定义中心坐标
#绘制标签:
lb = Label(text="代码编写:  daode1212, 2021-10-22", fg="#003399", bg="#FFEE88")
lb.config(bd=5,relief = SUNKEN);lb.pack(side="bottom")
#预装图片：
photo1 =PhotoImage(file = "eye.png");photo2 =PhotoImage(file = "boy.png")

#动画绘制函数-A:
def myDrawA():
    for g in range(-1200,1200,1):
        w.delete("all")
        x=400*math.cos(g/91)
        w.create_image(x0+x, y0, image = photo1)
        w.update();time.sleep(0.001)
#动画绘制函数-B:
def myDrawB():
    for g in range(-1200,1200,1):
        w.delete("all")
        h=250*math.cos(g/31)
        w.create_image(x0, y0+h, image = photo1)
        w.update();time.sleep(0.001)
#动画绘制函数-C:
def myDrawC():
    for g in range(-1200,1200,1):
        w.delete("all")
        dx=250*math.cos(g/31)
        dy=250*math.sin(g/31)
        w.create_image(x0+dx, y0+dy, image = photo1)
        w.update();time.sleep(0.001)
#动画绘制函数-D:
def myDrawD():
    r = 250
    for g in range(-200,200,1):
        w.delete("all")
        u=3600
        rgb ='#'+ str(hex(rnd.randint(0x888888, 0xFFFFFF)))[2:]  # 生成随机颜色
        while u > 0:
            x1, y1 = r*math.cos((g+u+3)/35), r*math.sin((g-u+3)/40)
            x2, y2 = r*math.cos((g+u)/35), r*math.sin((g-u)/40)
            xd=x2*math.cos(g/45)-y2*math.sin(g/45)
            yd=x2*math.sin(g/45)+y2*math.cos(g/45)
            w.create_image(x0+xd, y0+yd, image = photo1)
            u -= 10
        w.update()
        time.sleep(0.001)
#动画绘制函数-E:
def myDrawE():
    r = 250
    for g in range(-200,200,1):
        w.delete("all")
        u=1200
        while u > 0:
            rgb ='#'+ str(hex(rnd.randint(0x888888, 0xFFFFFF)))[2:]  # 生成随机颜色
            x1, y1 = r * math.cos((g+u+3) / 23), r * math.sin((g-u+3) / 23)
            x2, y2 = r * math.cos((g+u) / 23), r * math.sin((g-u) / 23)
            x3=x1*math.cos(g / 45)-y1*math.sin(g / 45)
            y3=x1*math.sin(g / 45)+y1*math.cos(g / 45)
            x4=x2*math.cos(g / 45)-y2*math.sin(g / 45)
            y4=x2*math.sin(g / 45)+y2*math.cos(g / 45)
            w.create_image(x0+x4, y0+y4, image = photo2)
            w.create_line(x0+1.7*x4, y0+1.7*y4, x0+1.3*x3, y0+1.3*y3, fill=rgb, width=8)
            u -= 10
        w.update()
        time.sleep(0.001)

#布局各按钮:
Button(root, text="[按钮A:水平移动]", command=(lambda: myDrawA()),
compound="center").pack(side="left")
Button(root, text="[按钮B:上下移动]", command=(lambda: myDrawB()),
compound="center").pack(side="left")
Button(root, text="[按钮C:圆周运动]", command=(lambda: myDrawC()),
compound="center").pack(side="left")
Button(root, text="[按钮D:曲线运动]", command=(lambda: myDrawD()),
compound="center").pack(side="left")
Button(root, text="[按钮E:运动花环]", command=(lambda: myDrawE()),
compound="center").pack(side="left")
root.mainloop()#启动主程序
