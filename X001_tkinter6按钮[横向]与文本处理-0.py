# 在这里写上你的代码 :-)

import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()

root.title("数学函数作图器")
w = tk.Canvas(root, width =800, height = 600)
w.pack()
x0,y0=400,300
lb=tk.Label(text="---------by daode1212  2021-04-06-----------", fg="black", bg="white").pack(side='bottom')

def myDraw1():
    w.create_text(80,20,text='4+6='+str(4+6))

def myDraw2():
    a=range(11)
    w.create_text(80,40,text=list(a))

def myDraw3():
    s=0
    for i in range(101):
        s+=i
    w.create_text(80, 60, text='1+2+3+...+100='+str(s))

def myDraw4():
    s=input('cat,dog,fox中任意选一动物:')
    w.create_text(80, 80, text='你所选择的是:'+s)

def myDraw5():
    f = float(input('圆的半径是:'))
    pi=3.14159265
    w.create_text(80, 100, text=f'圆的周长与面积分别是{2*f*pi},{pi*f*f}')

def myDraw6():
    f = float(input('球的半径是:'))
    pi = 3.14159265
    s=f'球的体积的面积分别是{4*pi*f*f*f/3},{4*pi*f*f}'
    messagebox.showinfo(title='aaa', message=s)
    w.create_text(80, 100, text=s)
    print(s)

def myDel():
    print('删除全部')
    #删除全部的用:
    w.delete('all')

tk.Button(root, text = "表达式计算", command = (lambda: myDraw1())).pack(side='left')
tk.Button(root, text = "区间与列表", command = (lambda: myDraw2())).pack(side='left')
tk.Button(root, text = "自然数求和", command = (lambda: myDraw3())).pack(side='left')
tk.Button(root, text = "选择动物", command = (lambda: myDraw4())).pack(side='left')
tk.Button(root, text = "圆周长与面积", command = (lambda: myDraw5())).pack(side='left')
tk.Button(root, text = "球的体积的面积", command = (lambda: myDraw6())).pack(side='left')

tk.Button(root, text = "删除全部图", command = (lambda : myDel())).pack(side='left')

root.mainloop()
