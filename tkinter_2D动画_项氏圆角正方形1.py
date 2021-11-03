from math import *;from tkinter import *;import random as rnd;
# 使用tkinter绘图:
root = Tk();canvas = Canvas(width=1200, height=800, bg="#000");
canvas.pack();
x0=600;y0=350;m=57.3;k13=20;
k1=1;k2=1;k3=1;k4=1;
k9=.1;k10=.1;k11=3;k12=3;
def sign(x): #项氏符号函数
    if x>0:
        return 1
    if x<0:
        return -1
    if x==0:
        return 0
for t in range(0, 3600, 1):  # 总循环多少次
    g=t/m;R=180+t/k13
    rgb = "#" + str(hex(0x100000+(t**2)%0xEFFFFF))[2:]  # 生成随机颜色
    canvas.create_oval(
    x0-5+R*sign(cos(g))*pow(cos(k1*g)*cos(k1*g),k12),
    y0-5-R*sign(sin(g))*pow(sin(k2*g)*sin(k2*g),k11),
    x0+5+R*sign(cos(g))*pow(cos(k3*g)*cos(k3*g),k10),
    y0+5-R*sign(sin(g))*pow(sin(k4*g)*sin(k4*g),k9),
    width=1, fill=rgb)
    canvas.update()#画布更新
root.mainloop()

