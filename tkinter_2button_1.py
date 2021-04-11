# 在这里写上你的代码 :-)
from tkinter import *

window = Tk()
window.title("First Window")
window.geometry("350x200")


lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)


txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()


def f1():
    res = "Welcome to 1" + txt.get()
    lbl.configure(text=res)

btn1 = Button(window, text="Click Me 1", command=f1)
btn1.grid(column=2, row=1)

def f2():
    res = "Welcome to 2" + txt.get()
    lbl.configure(text=res)

btn2 = Button(window, text="Click Me 2", command=f2)
btn2.grid(column=3, row=1)

window.mainloop()
