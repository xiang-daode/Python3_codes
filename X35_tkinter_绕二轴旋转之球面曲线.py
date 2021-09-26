from math import *;from tkinter import *;import random as rnd;

# 使用tkinter绘图:
root = Tk()
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()
x0=600;y0=400;m=57.3;x1=x0;y1=y0

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
        xc=R*cos(g*5)*cos(g*13)
        yc=R*sin(g*5)*cos(g*13)
        zc=R*sin(g*13)

        #绕Y轴旋转空间点：
        x2=xc*cos(s)-zc*sin(s)
        y2=yc
        z2=xc*sin(s)+zc*cos(s)

        #绕X轴旋转空间点：
        x3=x2
        y3=y2*cos(s/4)-z2*sin(s/4)
        z3=y2*sin(s/4)+z2*cos(s/4)

        #以线段集方式绘制曲线：
        canvas.create_line(x0+x1,y0+y1,x0+x3,y0+y3,
            tag="L_" + str(t), width=4, fill=rgb)
        x1=x3;y1=y3 #替换线段起点

    #画布更新:
    canvas.update()

    # 重绘前删除已经绘制图像:
    for t in range(0, 365, 1):
        canvas.delete("L_" + str(t))

root.mainloop()

