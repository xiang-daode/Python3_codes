#
import math; import time; from tkinter import *; import random as rnd;
root = Tk()# 使用tkinter绘图:
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()
a,b,c,d,e,f=33, 27, 29, 29, 2.5, 6
for t in range(0, 3600, 1):  # 总循环多少次
    for k in range(t, t + 37):  # 每次生成多少个
        xt = 600 * (1 + 0.75 * math.cos(k / a))
        yt = 400 * (1 + 0.75 * math.sin(k / b))
        k2 = k - e
        xt2 = 600 * (1 + 0.75 * math.cos(k2 / c))
        yt2 = 400 * (1 + 0.75 * math.sin(k2 / d))
        rgb = "#" + str(hex(rnd.randint(0x100000, 0xFF00FF)))[2:]  # 生成随机颜色
        #rgb = "#" + str(hex(0x100000+t**4%0xEFFFFF))[2:]  # 生成随机颜色
        canvas.create_line(xt, yt, xt2, yt2, tag="pic" + str(k), width=f, fill=rgb)
    #画布更新:
    canvas.update()
    # 删除图像,以重绘:
    for k in range(t, t + 27):
        canvas.delete("pic" + str(k))
root.mainloop()
