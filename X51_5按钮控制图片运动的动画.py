import math;import time;
import random as rnd;from tkinter import *
#定义画布:
root = Tk();root.title("[python+tkinter]动画设计器")
w = Canvas(root, width=1200, height=600, bg="#FFF");w.pack()
x0, y0 = 600, 300 #定义中心坐标
#绘制标签:
lb = Label(text="代码编写:  daode1212, 2021-10-22", fg="#003399", bg="#FFEE88")
lb.config(bd=5,relief = SUNKEN);lb.pack(side="bottom")
#预装图片(先画两张图片:"eye.png","boy.png"，大小：100*100)：
photo1 =PhotoImage(file = "eye.png");photo2 =PhotoImage(file = "boy.png")

#动画绘制函数-A:
def myDrawA():
    for g in range(-1200,1200,1):
        w.delete("all")
        x=400*math.cos(g/91)
        w.create_image(x0+x, y0, image = photo1)
        w.update();time.sleep(0.001)
#动画绘制函数-B:
def myDrawB():
    for g in range(-1200,1200,1):
        w.delete("all")
        h=250*math.cos(g/31)
        w.create_image(x0, y0+h, image = photo1)
        w.update();time.sleep(0.001)
#动画绘制函数-C:
def myDrawC():
    for g in range(-1200,1200,1):
        w.delete("all")
        dx=250*math.cos(g/31)
        dy=250*math.sin(g/31)
        w.create_image(x0+dx, y0+dy, image = photo1)
        w.update();time.sleep(0.001)
#动画绘制函数-D:
def myDrawD():
    r = 250 #绘图半径
    for g in range(-200,200,1):
        w.delete("all") #清除全部
        u=3600 #被减数
        rgb ='#'+ str(hex(rnd.randint(0x888888, 0xFFFFFF)))[2:]  # 生成随机颜色
        while u > 0:#此条件下画图：
            x, y = r*math.cos((g+u)/45), r*math.sin((g-u)/45)#计算X，Y坐标
            xd=x*math.cos(g/45)-y*math.sin(g/45)#旋转变换
            yd=x*math.sin(g/45)+y*math.cos(g/45)#旋转变换
            w.create_image(x0+xd, y0+yd, image = photo1)#放入图片
            u -= 10#每一次减10，速度
        w.update()#更新画布
        time.sleep(0.001)
#动画绘制函数-E:
def myDrawE():
    r = 250
    for g in range(-200,200,1):
        w.delete("all")
        u=1200
        while u > 0:
            rgb ='#'+ str(hex(rnd.randint(0x888888, 0xFFFFFF)))[2:]  # 生成随机颜色
            x1, y1 = r * math.cos((g+u) / 32), r * math.sin((g+u) / 24)#计算X，Y坐标
            x2=x1*math.cos(g / 45)-y1*math.sin(g / 45)#旋转变换
            y2=x1*math.sin(g / 45)+y1*math.cos(g / 45)#旋转变换
            w.create_image(x0+x2, y0+y2, image = photo2) #放入图片
            w.create_line(x0, y0, x0+x2, y0+y2, fill=rgb, width=4) #画线段
            u -= 10#每一次减10，速度
        w.update()#更新画布
        time.sleep(0.001)#暂停0.001秒

#布局各按钮:
Button(root, text="[按钮A:水平移动]", command=(lambda: myDrawA()),
compound="center").pack(side="left")
Button(root, text="[按钮B:上下移动]", command=(lambda: myDrawB()),
compound="center").pack(side="left")
Button(root, text="[按钮C:圆周运动]", command=(lambda: myDrawC()),
compound="center").pack(side="left")
Button(root, text="[按钮D:曲线运动]", command=(lambda: myDrawD()),
compound="center").pack(side="left")
Button(root, text="[按钮E:运动花环]", command=(lambda: myDrawE()),
compound="center").pack(side="left")
root.mainloop()#启动主程序
