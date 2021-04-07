from tkinter import *
import math






top = Tk()
top.geometry("1200x750")
w = Canvas(top, width =1200, height = 600)
w.pack()
x0,y0=600,300


# 定义函数在先:
def selection():
    si = str(radio.get())
    # label.config(text=si)
    w.delete('all')
    if si == '1':
        label.config(text=si + ',极坐标系')
        pts = []
        for q in range(0,5*360,2):
            g=math.pi*q/180.0
            x =x0+220*math.cos(g)*math.cos(6*g)
            y =y0+220*math.sin(g)*math.cos(6*g)
            pts.append(x)
            pts.append(y)
        w.create_polygon(pts,outline="red",fill="#004488")
        w.create_text(120, 80, text='当中画了个多叶图')
    elif si == '2':
        label.config(text=si + ',极坐标系')
        pts = []
        for q in range(0, 5 * 360, 2):
            g = math.pi * q / 180.0
            x = x0 + 120 * math.cos(g) + 155 * math.cos(17 * g)
            y = y0 + 120 * math.sin(g) + 155 * math.sin(17 * g)
            pts.append(x)
            pts.append(y)
        w.create_polygon(pts, outline="red", fill="#004488")
        w.create_text(120, 100, text='当中画了个魔镜图')
    elif si == '3':
        label.config(text=si + ',直角坐标系')
        r = 150
        for x in range(0, 1200, 5):
            x1, x2 = x - 5, x + 5
            y1, y2 = y0 + r * math.sin(x / 100), y0 + r * math.sin(x / 101)
            w.create_oval(x1, y1, x2, y2, fill="#F40F04")
        w.create_text(120, 120, text='画了个波形图')
    elif si == '4':
        label.config(text=si + ',直角坐标系')
        r = 150
        for x in range(0, 1200, 5):
            x1, x2 = x - 5, x + 5
            y1, y2 = y0 - r * math.sin(12345/(x+ 47)), y0 + r *math.sin(12345/(x+ 73))
            w.create_rectangle(x1, y1, x2, y2, fill="#F4FF04")
        w.create_text(120, 140, text='画了个波形图')
    else:
        pass

radio = IntVar()

#用于提示信息:
lbl = Label(text="绘图要学好数学\n============================================")
lbl.pack(side='left')

#以下N个单选钮:
R1 = Radiobutton(top, text="绘图1", variable=radio, value=1,command=selection)
R1.pack(side='left')

R2 = Radiobutton(top, text="绘图2", variable=radio, value=2,command=selection)
R2.pack(side='left')

R3 = Radiobutton(top, text="绘图3", variable=radio, value=3,command=selection)
R3.pack(side='left')

R4 = Radiobutton(top, text="绘图4", variable=radio, value=4,command=selection)
R4.pack(side='left')

#用于输出显示:
label = Label(top,text='============',bg='#FFEEAA',width=40)
label.pack(side='left')

top.mainloop()