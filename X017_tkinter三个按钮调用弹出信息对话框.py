# 三个按钮调用弹出信息对话框:
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("First Window ---by daode1212")
window.geometry("350x200")

def f01():
    messagebox.showinfo("title", "1-->{一}")
btn1 = Button(window, text="f1", command=f01)
btn1.grid(column=1, row=0)

def f02():
    messagebox.showinfo("title", "2-->{二}")
btn2 = Button(window, text="f2", command=f02)
btn2.grid(column=2, row=0)

def f03():
    messagebox.showinfo("title", "3-->{三}")
btn3 = Button(window, text="f3", command=f03)
btn3.grid(column=3, row=0)



window.mainloop()
