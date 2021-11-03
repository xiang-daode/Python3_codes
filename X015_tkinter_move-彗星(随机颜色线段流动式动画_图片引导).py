# 要素:线段,矩形,图片,动画(延时与擦除),随机颜色,二维曲线
import math
import time
from tkinter import *
import random as rnd

# 使用tkinter绘图:
root =Tk()
canvas =Canvas(width=1200, height=800, bg='#FFF')
canvas.pack()

# 加载图片:
photo1 =PhotoImage(file = "O.png")

for t in range(0,3600,1):# 总循环多少次
    xt = 600 * (1 + math.cos(t / 32.3))
    yt = 400 * (1 + math.sin(t / 23.7))
    canvas.create_image(xt, yt, image=photo1, tag="pic")

    for k in range(t,t-50,-1):# 每次生成多少个
        xt=600*(1+math.cos(k/32.3))
        yt=400*(1+math.sin(k/23.7))
        k2=k+1
        xt2=600*(1+math.cos(k2/32.3))
        yt2=400*(1+math.sin(k2/23.7))
        #生成随机颜色:
        rgb1='#' + str(hex(rnd.randint(0x100000, 0xffffff)))[2:]
        rgb2 ='#' + str(hex(rnd.randint(0x100000, 0xffffff)))[2:]

        canvas.create_rectangle(xt, yt, xt2, yt2, tag="pic_" + str(k),fill=rgb1)
        canvas.create_line(xt, yt, xt2, yt2, tag="pic" + str(k), width=5, fill=rgb2)

        canvas.update()
    # 暂停n秒，然后删除图像:
    time.sleep(0.01)
    canvas.delete("pic")
    for k in range(t,t-50,-1):
        canvas.delete("pic"+str(k))
        canvas.delete("pic_"+str(k))
root.mainloop()
