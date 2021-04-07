# 在这里写上你的代码 :-)

import tkinter as tk

root = tk.Tk()
root.title("数学函数作图器")
w = tk.Canvas(root, width =1200, height = 600)
w.pack()
x0,y0=600,300
lb=tk.Label(text="---------by daode1212  2021-04-06-----------", fg="black", bg="white").pack(side='bottom')

def myDrawA():
    import math
    r=150
    for x in range(0,1200,5):
       x1,x2=x-5,x+5
       y1,y2=y0-r*math.sin(x/60) ,y0+r*math.sin(x/60)
       w.create_rectangle(x1, y1, x2, y2, fill = "#00FF44")

def myDrawB():
    import math
    r=150
    for x in range(0,1200,5):
       x1,x2=x-5,x+5
       y1,y2=y0-r*math.sin(x/80) ,y0+r*math.sin(x/80)
       w.create_rectangle(x1, y1, x2, y2, fill = "#4F00F4")

def myDrawC():
    import math
    r=150
    for x in range(0,1200,5):
       x1,x2=x-5,x+5
       y1,y2=y0-r*math.sin(x/100) ,y0+r*math.sin(x/100)
       w.create_rectangle(x1, y1, x2, y2, fill = "#F40F04")

def myDel():
    print('删除全部')
    w.delete('all')

photo = tk.PhotoImage(file = '按钮.png')
tk.Button(root, text="[按钮A]", command = (lambda: myDrawA()), image = photo, compound = "center").pack(side='left')
tk.Button(root, text="[按钮B]", command = (lambda: myDrawB()), image = photo, compound = "center").pack(side='left')
tk.Button(root, text="[按钮C]", command = (lambda: myDrawC()), image = photo, compound = "center").pack(side='left')
tk.Button(root, text = "删除全部图", command = (lambda : myDel())).pack(side='left')

root.mainloop()
