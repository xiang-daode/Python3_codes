from math import *;
from tkinter import *;
import random as rnd;

# 使用tkinter绘图:
root = Tk()
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()
x0=600;y0=400;m=57.3
x1=x0;y1=y0
def sign(x):
    if x>0:
        return 1
    if x<0:
        return -1
    if x==0:
        return 0
canvas.create_oval(x0-225,    y0-225,    x0+225,    y0+225,
tag="p_" + str(0), width=1, fill="#202060")
s=0.0
while s<3600:
    s=s+0.05
    for t in range(0, 365, 1):  # 总循环多少次
        g=t/57.3;R=200
        rgb = "#"+str(hex(0x700000+t**2%0x8FFFFF))[2:]  # 生成随机颜色

        xc=R*cos(g*7)*cos(g*4)
        yc=R*sin(g*7)*cos(g*4)
        zc=R*sin(g*4)

        x2=xc*cos(s)-zc*sin(s)
        y2=yc
        z2=xc*sin(s)+zc*cos(s)

        x3=x2
        y3=y2*cos(s/4)-z2*sin(s/4)
        z3=y2*sin(s/4)+z2*cos(s/4)

        if t>0:
            canvas.create_line(x0+x1,y0+y1,x0+x3,y0+y3,
            tag="L_" + str(t), width=8, fill=rgb)
        x1=x3;y1=y3

    #画布更新:
    canvas.update()

    # 删除图像,以重绘:
    for t in range(0, 365, 1):
        canvas.delete("L_" + str(t))


root.mainloop()

