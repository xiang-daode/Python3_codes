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

a,b,c=-300,300,3 #画球旋转角范围:起点,终点,步长
e,f,g=153,39,129 #画球形状控制参数
t=0
while True:  # 总循环多少次
    rgb ='#'+ str(hex(rnd.randint(0x888888, 0xFFFFFF)))[2:]  # 生成随机颜色

    for k in range(a,b,c):  # 每次生成多少个
        #生成球面点集:
        xt = 0.45 * math.cos(k / e)* math.cos(k / f)
        yt = 0.45 * math.sin(k / e)* math.cos(k / f)
        zt = 0.45 * math.sin(k / f)
        #绕Y轴旋转:
        x2=xt*math.cos(t / g)-zt*math.sin(t / g)
        y2=yt
        z2=xt*math.sin(t / g)+zt*math.cos(t / g)
        #平移与缩放:
        x3=400 * (1.3 + x2)
        y3=400 * (1 + y2)
        #绘制圆片:
        canvas.create_oval(
            x3-5, y3-5, x3+5, y3+5, tag="pic" + str(k), fill=rgb
        )


    #更新画布:
    canvas.update()

    # 删除图像,以重绘:
    #time.sleep(0.01)
    for k in range(a,b,c):
        canvas.delete("pic" + str(k))
    t+=2 #速度控制

root.mainloop()
