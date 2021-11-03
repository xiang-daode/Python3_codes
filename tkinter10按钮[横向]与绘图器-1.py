import tkinter as tk;import math;from tkinter import *
#先制作图片：按钮.png
root = tk.Tk();root.title("数学函数作图器");x0,y0=400,300
w = tk.Canvas(root, width =900, height = 600);w.pack()
#版权标签：
lb=tk.Label(text="---by daode1212  2021-10-23---", fg="black", bg="white").pack(side='bottom')
#自编函数N个：
def myDraw1():
    w.create_line(0, 300, 800, 300, fill = "red", dash = (2, 2))
    w.create_line(400, 0, 400, 600, fill = "blue", dash = (3, 3))
    w.create_text(80,20,text='画二条线段作坐标轴')
def myDraw2():
    w.create_rectangle(x0-25, y0-25, x0+25, y0+25, fill = "red")
def myDraw3():
    w.create_oval(155,155,255,255, fill="#44eeff")
def myDraw4():
    w.create_polygon(212,455,573,47,89,481,23,514,55,466,221,44, fill="gray")
def myDraw5():
    coord = 10, 50, 240, 210
    w.create_arc(coord, start=0, extent=60, fill="blue")
def myDraw6():
    r=150
    for x in range(0,800,5):
       x1,x2=x-5,x+5
       y1,y2=y0-r*math.sin(x/60) ,y0+r*math.sin(x/120)
       w.create_rectangle(x1, y1, x2, y2, fill = "#F4004F")
       w.create_text(80,40,text='这是绿色的矩形所组成的')
def myDrawA():
    r=150
    for x in range(0,800,5):
       x1,x2=x-5,x+5
       y1,y2=y0-r*math.sin(x/30) ,y0+r*math.sin(x/70)
       w.create_rectangle(x1, y1, x2, y2, fill = "#00F4F4")
def myDrawB():
    r=150
    for x in range(0,800,5):
       x1,x2=x-5,x+5
       y1,y2=y0-r*math.sin(x/160) ,y0+r*math.sin(x/80)
       w.create_rectangle(x1, y1, x2, y2, fill = "#40FF04")
def myDrawC():
    r=150
    for x in range(0,800,5):
       x1,x2=x-5,x+5
       y1,y2=y0-r*math.sin(x/60) ,y0+r*math.sin(x/180)
       w.create_rectangle(x1, y1, x2, y2, fill = "#F40F04")
def myDel():
    w.delete('all') #删除全部
#普通按钮：
tk.Button(root, text = "添加图形1", command = (lambda: myDraw1())).pack(side='left')
tk.Button(root, text = "添加图形2", command = (lambda: myDraw2())).pack(side='left')
tk.Button(root, text = "添加图形3", command = (lambda: myDraw3())).pack(side='left')
tk.Button(root, text = "添加图形4", command = (lambda: myDraw4())).pack(side='left')
tk.Button(root, text = "添加图形5", command = (lambda: myDraw5())).pack(side='left')
tk.Button(root, text = "添加图形6", command = (lambda: myDraw6())).pack(side='left')
#图片式按钮：
photo = tk.PhotoImage(file = '按钮.png')
tk.Button(root, text="[按钮A]", command = (lambda: myDrawA()), image = photo, compound = "center").pack(side='left')
tk.Button(root, text="[按钮B]", command = (lambda: myDrawB()), image = photo, compound = "center").pack(side='left')
tk.Button(root, text="[按钮C]", command = (lambda: myDrawC()), image = photo, compound = "center").pack(side='left')
#"删除全部图"按钮：
tk.Button(root, text = "删除全部图", command = (lambda : myDel())).pack(side='left')
root.mainloop()
