# 在这里写上你的代码 :-)
import math;import time;from tkinter import *;import random as rnd;

# 使用tkinter绘图:
root = Tk()
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()

for t in range(0, 3600, 1):  # 总循环多少次
    for k in range(t, t + 37):  # 每次生成多少个
        xt = 600 * (1 + 0.75 * math.cos(k / 12))
        yt = 400 * (1 + 0.75 * math.sin(k / 12))
        k2 = k - 1.3
        xt2 = 600 * (1 + 0.75 * math.cos(k2 / 12))
        yt2 = 400 * (1 + 0.75 * math.sin(k2 / 12))
        #rgb = "#" + str(hex(rnd.randint(0x100000, 0xFF00FF)))[2:]  # 生成随机颜色
        rgb = "#" + str(hex(0x100000+t*4321))[2:]  # 生成随机颜色
        canvas.create_line(
            xt, yt, xt2, yt2, tag="pic" + str(k), width=6, fill=rgb
        )

    #画布更新:
    canvas.update()

    # 删除图像,以重绘:
    for k in range(t, t + 7):
        canvas.delete("pic" + str(k))

root.mainloop()
