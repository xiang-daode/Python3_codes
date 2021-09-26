from math import *;from tkinter import *;import random as rnd;

# 使用tkinter绘图:
root = Tk()
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()
x0=600;y0=400;m=57.3;xa=x0;yb=y0

#绘制背景圆：
canvas.create_oval(x0-225,    y0-225,    x0+225,    y0+225,
tag="p_" + str(0), width=1, fill="#006")

s=0.0
while s<3600: #总时间控制
    s=s+0.07 #旋转速度
    for t in range(0, 365, 1):  # 总循环多少次
        g=t/57.3;R=225
        rgb = "#"+str(hex(0x700000+t**2%0x8FFFFF))[2:]  # 生成随机颜色

        #生成球面曲线点：
        xc=R*cos(g*13)*cos(g*4)
        yc=R*sin(g*13)*cos(g*4)
        zc=R*sin(g*4)

        #绕Z轴旋转空间点：
        x1=xc*cos(s/2.00)-yc*sin(s/2.00)
        y1=xc*sin(s/2.00)+yc*cos(s/2.00)
        z1=zc

        #绕Y轴旋转空间点：
        x2=x1*cos(s/3.00)-z1*sin(s/3.00)
        y2=y1
        z2=x1*sin(s/3.00)+z1*cos(s/3.00)

        #绕X轴旋转空间点：
        x3=x2
        y3=y2*cos(s/4.00)-z2*sin(s/4.00)
        z3=y2*sin(s/4.00)+z2*cos(s/4.00)

        #以线段集方式绘制曲线：
        canvas.create_line(x0+xa,y0+yb,x0+x3,y0+y3,
            tag="L_" + str(t), width=4, fill=rgb)
        xa=x3;yb=y3 #替换线段起点

    #画布更新:
    canvas.update()

    # 重绘前删除已经绘制图像:
    for t in range(0, 365, 1):
        canvas.delete("L_" + str(t))

root.mainloop()

