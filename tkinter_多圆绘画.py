from math import *;from tkinter import *;import random as rnd;
# 使用tkinter绘图:
root = Tk();canvas = Canvas(width=1200, height=800, bg="#000");
canvas.pack();x0=600;y0=350;m=57.3
k1=17;k2=28;k3=17.002;k4=28.002;
k5=17;k6=28;k7=17;k8=28;

for t in range(0, 3600, 2):  # 总循环多少次
    g=t/m;R=360+t/30
    rgb = "#" + str(hex(0x100000+(t**2)%0xEFFFFF))[2:]  # 生成随机颜色
    canvas.create_oval(
    x0-5+R*cos(k1*g)+R*cos(k5*g)/4,
    y0-5-R*sin(k2*g)+R*sin(k6*g)/4,
    x0+5+R*cos(k3*g)+R*cos(k7*g)/4,
    y0+5-R*sin(k4*g)+R*sin(k8*g)/4,
    width=1, fill=rgb)
    canvas.update()     # 画布更新
root.mainloop()

