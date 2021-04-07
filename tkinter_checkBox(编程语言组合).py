# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import messagebox
import tkinter


top = tkinter.Tk()
top.geometry('1200x200+600+100')#宽度,高度,x,y

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

# 必须定义函数在前,函数调用在后:
def myFun():
    s=str(8*CheckVar1.get()+4*CheckVar2.get()+2*CheckVar3.get()+CheckVar4.get())
    L2.config(text=s)
    #messagebox.showinfo('可执行相应任务(0,1,2,3,...,15):',s)
    #根据s的值分别执行相应任务(0,1,2,3,...,15):
    if s=='1':
        messagebox.showinfo('返回结果:',f'你是级别{s}!')
    elif s=='2':
        messagebox.showinfo('返回结果:',f'你是级别{s}!')
    elif s=='3':
        messagebox.showinfo('返回结果:',f'你是级别{s}!')
    elif s=='4':
        messagebox.showinfo('返回结果:',f'你是级别{s}!')
    elif s=='5':
        messagebox.showinfo('返回结果:',f'你是级别{s}!')
    elif s=='6':
        messagebox.showinfo('返回结果:',f'你是级别{s}!')
    elif s=='7':
        messagebox.showinfo('返回结果:',f'你是级别{s}!')
    elif s=='8':
        messagebox.showinfo('返回结果:',f'你是级别{s}!')
    else:
        messagebox.showinfo('返回结果:','你是大神级别!')


# 定义一些多选框:
# 必须定义函数在前,函数调用在后:
C1 = Checkbutton(top, text="H5,javaScript", variable=CheckVar1,
                 width=20,command=myFun).pack(side = 'left')
C2 = Checkbutton(top, text="Python", variable=CheckVar2,
                 width=20,command=myFun).pack(side = 'left')
C3 = Checkbutton(top, text="java", variable=CheckVar3,
                 width=20,command=myFun).pack(side = 'left')
C4 = Checkbutton(top, text="C,C++,C#", variable=CheckVar4, width=20,
                 command=myFun).pack(side = 'left')

#标签:
L2 = Label(top, bd =0,text='你已经掌握哪几种编程语言?')
L2.pack(side = 'left')

top.mainloop()