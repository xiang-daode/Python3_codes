# 在这里写上你的代码 :-)
# 在这里写上你的代码 :-)
import math
import time
from tkinter import *
import random as rnd

# 使用tkinter绘图:
root = Tk()
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()

# 加载图片:
# photo1 =PhotoImage(file = "Q.png")

for t in range(0, 3600, 1):  # 总循环多少次
    rgb = "#" + str(hex(rnd.randint(0x100000, 0xFF00FF)))[2:]  # 生成随机颜色

    for k in range(t, t + 60):  # 每次生成多少个
        xt = 600 * (1 + 0.75 * math.cos(k / 29))
        yt = 400 * (1 + 0.75 * math.sin(k / 27))
        k2 = k + 0.37
        xt2 = 600 * (1 + 0.75 * math.cos(k2 / 18))
        yt2 = 400 * (1 + 0.75 * math.sin(k2 / 16))

        canvas.create_line(
            xt, yt, xt2, yt2, tag="pic_" + str(k), width=3, fill=rgb
        )
        canvas.update()

    for k in range(t, t + 7):  # 每次生成多少个
        xt = 600 * (1 + 0.75 * math.cos(k / 29))
        yt = 400 * (1 + 0.75 * math.sin(k / 27))
        k2 = k - 0.17
        xt2 = 600 * (1 + 0.75 * math.cos(k2 / 18))
        yt2 = 400 * (1 + 0.75 * math.sin(k2 / 16))

        canvas.create_line(
            xt, yt, xt2, yt2, tag="pic" + str(k), width=12, fill=rgb
        )

    #画布更新:
    canvas.update()


    # 删除图像,以重绘:
    for k in range(t, t + 7):
        canvas.delete("pic" + str(k))
    for k in range(t, t + 60):
        canvas.delete("pic_" + str(k))


root.mainloop()
