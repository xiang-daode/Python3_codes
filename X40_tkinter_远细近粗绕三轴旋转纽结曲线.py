from math import *;from tkinter import *;import random as rnd;
# 算法设计：项道德（daode1212,daode3056），2021-09-26
# 使用tkinter绘图:
root = Tk()
canvas = Canvas(width=1200, height=800, bg="#000")
canvas.pack()
x0=600;y0=400;xa=x0;yb=y0

#绘制背景圆：
canvas.create_oval(x0-225,    y0-225,    x0+225,    y0+225,
tag="p_" + str(0), width=1, fill="#006")

s=0.0
while s<3600: #总时间控制
    s=s+0.01 #旋转速度
    for t in range(0, 3600, 10):  # 总循环多少次
        g=s+t/300;

        #生成曲线点：
        R=225
        xc=R*cos(g*6)
        yc=R*sin(g*5)
        zc=R*sin(g*4)

        #绕Z轴旋转空间点：
        x1=xc*cos(s/2)-yc*sin(s/2)
        y1=xc*sin(s/2)+yc*cos(s/2)
        z1=zc

        #绕Y轴旋转空间点：
        x2=x1*cos(s*3)-z1*sin(s*3)
        y2=y1
        z2=x1*sin(s*3)+z1*cos(s*3)

        #绕X轴旋转空间点：
        x3=x2
        y3=y2*cos(s/4)-z2*sin(s/4)
        z3=y2*sin(s/4)+z2*cos(s/4)

        #处理远近，以不同的粗细与颜色呈现，再以线段集方式绘制曲线:
        rgb = "#"+str(hex(0xD00000+t%0x2FFFFF))[2:]  # 生成颜色
        if z3<0:
            rgb="#224"; #背面曲线颜色
        if t>0:
            canvas.create_line(x0+xa,y0+yb,x0+x3,y0+y3,
                tag="L_" + str(t), width=(z3/20 if z3>0 else 2) , fill=rgb)
        xa=x3;yb=y3 #替换线段起点

    #画布更新:
    canvas.update()

    # 重绘前删除已经绘制图像:
    for t in range(0, 3600, 5):
        canvas.delete("L_" + str(t))

root.mainloop()

