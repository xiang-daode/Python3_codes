# 在这里写上你的代码 :-)
import math
import time
from tkinter import *
import random as rnd

# 使用tkinter绘图:
root =Tk()
canvas =Canvas(width=1200, height=800, bg='white')
canvas.pack()

# 加载图片:
# photo1 =PhotoImage(file = "Q.png")

for t in range(0,3600,1):# 总循环多少次
    for k in range(t-15,t+15):# 每次生成多少个
        xt=600*(1+math.cos(k/123))
        yt=400*(1+math.sin(k/137))
        k2=k+1
        xt2=600*(1+math.cos(k2/123))
        yt2=400*(1+math.sin(k2/137))
        #生成随机颜色:
        rgb1='#' + str(hex(rnd.randint(0x100000, 0xffffff)))[2:]
        rgb2 ='#' + str(hex(rnd.randint(0x100000, 0xffffff)))[2:]
        canvas.create_rectangle(xt, yt, xt2, yt2, tag="pic_" + str(k),fill=rgb1)
        canvas.create_line(xt, yt, xt2, yt2, tag="pic" + str(k), width=5,
                           fill=rgb2)
        canvas.update()
    # 暂停n秒，然后删除图像:
    # time.sleep(0.001)
    for k in range(t-15,t+15):
        canvas.delete("pic"+str(k))
        canvas.delete("pic_"+str(k))
root.mainloop()
