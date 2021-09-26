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
canvas.create_oval(x0-75,    y0-75,    x0+75,    y0+75,
tag="p_" + str(0), width=1, fill="#FF88FF")

for t in range(0, 3600, 1):  # 总循环多少次
    g=t/57.3;R=150+t/10
    rgb = "#"+str(hex(0x700000+t**9%0x8FFFFF))[2:]  # 生成随机颜色
    x2=x0+R*sign(cos(g))*pow(cos(g)*cos(g),2)
    y2=y0-R*sign(sin(g))*pow(sin(g)*sin(g),2)
    canvas.create_line(x1,y1,x2,y2,
    tag="L_" + str(t), width=8, fill=rgb)
    x1=x2;y1=y2

    #画布更新:
    canvas.update()

    # 删除图像,以重绘:
    #canvas.delete("L_" + str(t))

root.mainloop()

