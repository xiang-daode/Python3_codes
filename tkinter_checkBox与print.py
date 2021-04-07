# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import messagebox
import tkinter

top = tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
# 必须定义函数在前,函数调用在后:
def myF1():
    print('myF1 ok',CheckVar1.get(),CheckVar2.get())

def myF2():
    print('myF2 ok',CheckVar1.get(),CheckVar2.get())

# 必须定义函数在前,函数调用在后:
C1 = Checkbutton(top, text="大海捞针", variable=CheckVar1, \
                 onvalue=1, offvalue=0, height=5, \
                 width=20,command=myF1)
C2 = Checkbutton(top, text="亡羊补牢", variable=CheckVar2, \
                 onvalue=1, offvalue=0, height=5, \
                 width=20,command=myF2)
C1.pack(side='left')
C2.pack(side='left')

top.mainloop()