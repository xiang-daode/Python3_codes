from math import *;
from tkinter import *;
import random as rnd;

# 使用tkinter绘图:
root = Tk()
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()

for t in range(0, 7200, 5):  # 总循环多少次
    rgb = "#" + str(hex(0x100000+t*6789))[2:]  # 生成随机颜色
    canvas.create_oval(t%600, t%400, 1200-t%600, 800-t%400, tag="p_" + str(t), width=1, fill=rgb)

    #画布更新:
    canvas.update()

    # 删除图像,以重绘:
    #canvas.delete("p_" + str(t))

root.mainloop()
