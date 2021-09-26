from math import *;
from tkinter import *;
import random as rnd;

# 使用tkinter绘图:
root = Tk()
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()
R=300
for t in range(0, 3600, 7):  # 总循环多少次
    rgb = "#" + str(hex(0x100000+t*6789))[2:]  # 生成随机颜色
    g=t/57.3
    xc=R*cos(g/6)
    yc=R*sin(g/4)
    canvas.create_oval(600-xc, 400-yc, 600+xc, 400+yc, tag="p_" + str(t), width=6, fill=rgb)

    #画布更新:
    canvas.update()

    # 删除图像,以重绘:
    #canvas.delete("p_" + str(t))

root.mainloop()
