# 在这里写上你的代码 :-)
import math
import time
import tkinter as tk

root = tk.Tk()
root.title("动画设计器 ----设计:项道德")
w = tk.Canvas(root, width=1200, height=600)
w.pack()
x0, y0 = 600, 300
lb = tk.Label(
    text="---------by daode1212  2021-04-06-----------", fg="#993300", bg="#00EEFF"
).pack(side="bottom")


def myDrawA(u):
    r = 150
    while u < 1000:
        x1, y1 = x0, y0
        x2, y2 = x0 + r * math.cos(u / 60), y0 + r * math.sin(u / 60)
        w.create_line(x1, y1, x2, y2, fill="#00FF44", width=8)
        w.update()
        time.sleep(0.001)
        w.delete("all")
        u += 3


def myDrawB(u):
    r = 200
    while u < 1000:
        x1, y1 = x0, y0
        x2, y2 = x0 + r * math.cos(u / 160), y0 + r * math.sin(u / 160)
        w.create_line(x1, y1, x2, y2, fill="#0044FF", width=8)
        w.update()
        time.sleep(0.001)
        w.delete("all")
        u += 5


def myDrawC(u):
    r = 250
    while u < 1000:
        x1, y1 = x0, y0
        x2, y2 = x0 + r * math.cos(u / 90), y0 + r * math.sin(u / 60)
        w.create_line(x1, y1, x2, y2, fill="#FF0044", width=8)
        w.update()
        time.sleep(0.001)
        w.delete("all")
        u += 10


def myDrawD(u):
    r = 250
    while u < 1000:
        x1, y1 = x0, y0
        x2, y2 = x0 + r * math.cos(u / 90), y0 + r * math.sin(u / 60)
        w.create_line(x1, y1, x2, y2, fill="#FF4400", width=8)
        w.update()
        time.sleep(0.001)
        w.delete("all")
        u += 15


photo = tk.PhotoImage(file="按钮.png")
tk.Button(
    root, text="[按钮A]", command=(lambda: myDrawA(0)), image=photo, compound="center"
).pack(side="left")
tk.Button(
    root, text="[按钮B]", command=(lambda: myDrawB(0)), image=photo, compound="center"
).pack(side="left")
tk.Button(
    root, text="[按钮C]", command=(lambda: myDrawC(0)), image=photo, compound="center"
).pack(side="left")
tk.Button(
    root, text="[按钮D]", command=(lambda: myDrawD(0)), image=photo, compound="center"
).pack(side="left")

root.mainloop()
