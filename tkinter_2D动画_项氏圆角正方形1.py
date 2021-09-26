from math import *;
from tkinter import *;
import random as rnd;

# 使用tkinter绘图:
root = Tk()
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()
x0=600;y0=400;m=57.3

def sign(x):
    if x>0:
        return 1
    if x<0:
        return -1
    if x==0:
        return 0

for t in range(0, 3600, 1):  # 总循环多少次
    g=t/57.3;R=150+t/20
    rgb = "#" + str(hex(0x100000+(t**8)%0xEFFFFF))[2:]  # 生成随机颜色
    canvas.create_oval(
    x0-5+R*sign(cos(g))*pow(cos(g)*cos(g),0.2),
    y0-5-R*sign(sin(g))*pow(sin(g)*sin(g),0.2),
    x0+5+R*sign(cos(g))*pow(cos(g)*cos(g),0.2),
    y0+5-R*sign(sin(g))*pow(sin(g)*sin(g),0.2),
    tag="p_" + str(t), width=1, fill=rgb)

    #画布更新:
    canvas.update()

    # 删除图像,以重绘:
    #canvas.delete("p_" + str(t))

root.mainloop()

