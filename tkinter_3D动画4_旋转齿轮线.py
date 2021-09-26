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
#canvas.create_oval(x0-75,    y0-75,    x0+75,    y0+75,
#tag="p_" + str(0), width=1, fill="#FF88FF")
s=0.0
while s<3600:
    s=s+0.05
    for t in range(0, 360, 1):  # 总循环多少次
        g=t/57.3;R=200+(20 if t%10>5 else 0)
        rgb = "#"+str(hex(0x700000+t**2%0x8FFFFF))[2:]  # 生成随机颜色

        xc=R*cos(g)
        yc=R*sin(g)
        zc=R
        x2=xc*cos(s)-zc*sin(s)
        y2=yc
        zc=xc*sin(s)+zc*cos(s)
        if t>0:
            canvas.create_line(x0+x1,y0+y1,x0+x2,y0+y2,
            tag="L_" + str(t), width=8, fill=rgb)
        x1=x2;y1=y2

    #画布更新:
    canvas.update()

    # 删除图像,以重绘:
    for t in range(0, 360, 1):
        canvas.delete("L_" + str(t))


root.mainloop()

