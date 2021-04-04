# 在这里写上你的代码 :-)
from tkinter import *
import tkinter as tk
root = tk.Tk()

w = tk.Canvas(root, width =800, height = 600,bg="#DEEEFF")
w.pack()

#画一条黄色的横线
w.create_line(0, 450, 600, 450, fill = "yellow")

#画一条红色的竖线（虚线）
w.create_line(400, 0, 400, 600, fill = "red", dash = (4, 4))

#中间画一个蓝色的矩形
w.create_rectangle(450, 425, 650, 675, fill = "blue")

# 创建一个矩形，坐标为(20,20,300,240)
w.create_rectangle(20,20,300,240)

#arc − 创建一个扇形
coord = 10, 50, 240, 210
w.create_arc(coord, start=0, extent=60, fill="blue")

#image − 创建图像
filename = PhotoImage(file = "按钮.png")
w.create_image(450, 550, anchor=NE, image=filename)

#line − 创建线条
w.create_line(60,360,200,100,  fill="#eff44e", width=8)

#oval − 创建一个圆
w.create_oval(155,155,255,255, fill="#44eeff")

#polygon − 创建一个至少有三个顶点的多边形
w.create_polygon(212,455,573,47,89,481,23,514,55,466,221,44, fill="gray")

cv.pack()
