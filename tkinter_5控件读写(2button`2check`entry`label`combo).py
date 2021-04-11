# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import messagebox
import tkinter
import tkinter as tk

top = tkinter.Tk()
top.geometry('1200x800+400+100')

# 创建一个Canvas，设置其背景色为白色
cv = Canvas(top,bg = 'white')
# 创建一个矩形，坐标为(x1,y1,x2,y2)
cv.create_rectangle(10,10,466,325)
cv.pack()

CheckVar1 = IntVar()
CheckVar2 = IntVar()


# 必须定义函数在前,函数调用在后:
def myF1():
    print('myF1 ok',CheckVar1.get(),CheckVar2.get(),E1.get())
    L2.config(text="大功告成!!!"+E1.get())



def myF2():
    print('myF2 ok',CheckVar1.get(),CheckVar2.get(),E1.get())
    L2.config(text="旗开得胜!!!"+E1.get())


# 必须定义函数在前,函数调用在后:
C1 = Checkbutton(top, text="大海捞针", variable=CheckVar1, \
                 onvalue=1, offvalue=0, height=5, \
                 width=20,command=myF1)
C2 = Checkbutton(top, text="亡羊补牢", variable=CheckVar2, \
                 onvalue=1, offvalue=0, height=5, \
                 width=20,command=myF2)
C1.pack(side = 'left')
C2.pack(side = 'left')

#标签:
L2 = Label(top, bd =0,text='123456')
L2.pack() #side = 'bottom'
L1 = Label(top, text="数目?")
L1.pack(side = 'bottom')


#输入文本框:
E1 = Entry(top, bd =4)
E1.pack(side = 'bottom')

def myDraw1():
    cv.create_oval(466/2-50,325/2-50,466/2+50,325/2+50, fill="#44eeff")

def myDraw2():
    cv.create_oval(466 / 2 - 250, 325 / 2 - 250, 466 / 2 + 250, 325 / 2 + 250, fill="#eeff44")


Button(top, text = "添加图形1", command = (lambda: myDraw1())).pack(side='left')
Button(top, text = "添加图形2", command = (lambda: myDraw2())).pack(side='left')

top.mainloop()
