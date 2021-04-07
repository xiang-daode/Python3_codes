# 在这里写上你的代码 :-)
import math
import tkinter as tk

root = tk.Tk()

root.title("数学函数作图器")
w = tk.Canvas(root, width =1200, height = 600)
w.pack()
x0,y0=600,300
lb=tk.Label(text="---------by daode1212  2021-04-06-----------", fg="black", bg="white").pack(side='bottom')

def myDraw1():
    w.create_line(0, 300, 1200, 300, fill = "red", dash = (2, 2))
    w.create_line(600, 0, 600, 600, fill = "blue", dash = (3, 3))
    w.create_text(120,20,text='画二条线段作坐标轴')
    w.create_text(1180, 300-10, text='X')
    w.create_text(600+10, 20, text='Y')

def myDraw2():
    w.create_rectangle(x0-15, y0-15, x0+15, y0+15, fill = "red")
    w.create_text(120,40,text='红色小方块的中心是原点')

def myDraw3():
    w.create_oval(x0-5.0, y0-5.0, x0+5.0, y0+5.0, fill="#44eeff")
    w.create_text(120,60,text='当中画了个圆')

def myDraw4():
    pts=[]
    for q in range(0,5*360,2):
        g=math.pi*q/180.0
        x =x0+220*math.cos(g)*math.cos(6*g)
        y =y0+220*math.sin(g)*math.cos(6*g)
        pts.append(x)
        pts.append(y)
    w.create_polygon(pts,outline="red",fill="#004488")
    w.create_text(120, 80, text='当中画了个多叶图')

def myDraw5():
    pts=[]
    for q in range(0,5*360,2):
        g=math.pi*q/180.0
        x =x0+120*math.cos(g)+155*math.cos(17*g)
        y =y0+120*math.sin(g)+155*math.sin(17*g)
        pts.append(x)
        pts.append(y)
    w.create_polygon(pts,outline="red",fill="#004488")
    w.create_text(120, 100, text='当中画了个魔镜图')

def myDraw6():
    r=150
    for x in range(0,1200,5):
       x1,x2=x-5,x+5
       y1,y2=y0-r*math.sin(x/100) ,y0+r*math.sin(x/100)
       w.create_rectangle(x1, y1, x2, y2, fill = "#00FF44")
       w.create_text(120,120,text='这是绿色的图是矩形所组成的')

def myDrawA():
    r=150
    for x in range(0,1200,5):
       x1,x2=x-5,x+5
       y1,y2=y0-r*math.sin(x/50) ,y0+r*math.sin(x/70)
       w.create_rectangle(x1, y1, x2, y2, fill = "#554400")
       w.create_text(120, 140, text='这是直角坐标系中的绘图A')

def myDrawB():
    r=150
    for x in range(0,1200,5):
       x1,x2=x-5,x+5
       y1,y2=y0+r*math.sin(x/78)*math.sin(x/37) ,y0+r*math.sin(x/78-1)*math.sin(x/37-1)
       w.create_rectangle(x1, y1, x2, y2, fill = "#4F00F4")
       w.create_text(120, 160, text='这是直角坐标系中的绘图B')

def myDrawC():
    r=150
    for x in range(0,1200,5):
       x1,x2=x-5,x+5
       y1,y2=y0+r*math.sin(x/56)*math.sin(x/33) ,y0+r*math.sin(x/53)*math.sin(x/31)
       w.create_rectangle(x1, y1, x2, y2, fill = "#ffee00")
       w.create_text(120, 180, text='这是直角坐标系中的绘图C')

def myDel():
    print('删除全部')
    w.delete('all')

tk.Button(root, text = "添加图形1", command = (lambda: myDraw1())).pack(side='left')
tk.Button(root, text = "添加图形2", command = (lambda: myDraw2())).pack(side='left')
tk.Button(root, text = "添加图形3", command = (lambda: myDraw3())).pack(side='left')
tk.Button(root, text = "添加图形4", command = (lambda: myDraw4())).pack(side='left')
tk.Button(root, text = "添加图形5", command = (lambda: myDraw5())).pack(side='left')
tk.Button(root, text = "添加图形6", command = (lambda: myDraw6())).pack(side='left')

photo = tk.PhotoImage(file = '按钮.png')
tk.Button(root, text="[按钮A]", command = (lambda: myDrawA()), image = photo, compound = "center").pack(side='left')
tk.Button(root, text="[按钮B]", command = (lambda: myDrawB()), image = photo, compound = "center").pack(side='left')
tk.Button(root, text="[按钮C]", command = (lambda: myDrawC()), image = photo, compound = "center").pack(side='left')

tk.Button(root, text = "删除全部图", command = (lambda : myDel())).pack(side='left')

root.mainloop()
