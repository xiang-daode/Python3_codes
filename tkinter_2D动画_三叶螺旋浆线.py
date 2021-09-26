from math import *;
from tkinter import *;
import random as rnd;
# 使用tkinter绘图:
root = Tk()
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()
x0=600;y0=400;m=57.3
for t in range(-720, 0, 1):  # 总循环多少次
    g=t/57.3;R=300*cos(3*g)
    rgb = "#" + str(hex(0x100000+(t**4)%0xEFFFFF))[2:]  # 生成随机颜色
    canvas.create_rectangle( # 或oval 或line 或rectangle
    x0-5+R*cos(g)-g*7,
    y0-5-R*sin(g)+g*5,
    x0+5+R*cos(g)+g*6,
    y0+5-R*sin(g)-g*4,
    tag="p_" + str(t), width=5, fill=rgb)
    #画布更新:
    canvas.update()
    # 删除图像,以重绘:
    #canvas.delete("p_" + str(t))
root.mainloop()
