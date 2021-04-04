# 在这里写上你的代码 :-)

import tkinter as tk



root = tk.Tk()

w = tk.Canvas(root, width =800, height = 500)
w.pack()
x0,y0=400,300

def myDraw1():
    w.create_line(0, 300, 800, 300, fill = "red", dash = (2, 2))
    w.create_line(400, 0, 400, 600, fill = "blue", dash = (3, 3))
def myDraw2():
    w.create_rectangle(x0-5, y0-5, x0+5, y0+5, fill = "red")

def myDraw3():
    w.create_oval(155,155,255,255, fill="#44eeff")
    #filename =  tk.PhotoImage(file = 'img.jpg')
    #w.create_image(300, 240, anchor='center', image=filename)

def myDraw4():
    w.create_polygon(212,455,573,47,89,481,23,514,55,466,221,44, fill="gray")

def myDraw5():
    coord = 10, 50, 240, 210
    w.create_arc(coord, start=0, extent=60, fill="blue")

def myDraw6():
    import math
    r=150
    for x in range(0,800,5):
       x1,x2=x-5,x+5
       y1,y2=y0-r*math.sin(x/100) ,y0+r*math.sin(x/100)
       w.create_rectangle(x1, y1, x2, y2, fill = "#00FF44")


def myDel():
    #按序号逐一删除的用:
    #for i in range(5):
    #    w.delete(i)
    #删除全部的用:
    w.delete('all')

tk.Button(root, text = "添加图形1", command = (lambda: myDraw1())).pack()
tk.Button(root, text = "添加图形2", command = (lambda: myDraw2())).pack()
tk.Button(root, text = "添加图形3", command = (lambda: myDraw3())).pack()
tk.Button(root, text = "添加图形4", command = (lambda: myDraw4())).pack()
tk.Button(root, text = "添加图形5", command = (lambda: myDraw5())).pack()
tk.Button(root, text = "添加图形6", command = (lambda: myDraw6())).pack()
tk.Button(root, text = "删除全部图", command = (lambda : myDel())).pack()
photo = tk.PhotoImage(file = '按钮.png')
tk.Button(root, text="点我", font = 20, image = photo, compound = "center").pack()


root.mainloop()
