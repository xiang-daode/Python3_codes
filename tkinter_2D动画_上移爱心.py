from math import *;
from tkinter import *;
import random as rnd;

# 使用tkinter绘图:
root = Tk()
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()
x0=600;y0=400;m=57.3
for s in range(-10, 10, 2):
    for t in range(-270, 270, 2):  # 总循环多少次
        g=t/57.3;R=t
        rgb = "#" + str(hex(0x100000+(t**4)%0xEFFFFF))[2:]  # 生成随机颜色
        canvas.create_oval(
        x0-5+R*cos(g),
        y0-5-R*sin(g)-s,
        x0+5+R*cos(g),
        y0+5-R*sin(g)-s,
        tag="p_" + str(t), width=1, fill=rgb)

        #画布更新:
        canvas.update()

        # 删除图像,以重绘:
        #canvas.delete("p_" + str(t))

root.mainloop()
