# 三个按钮调用弹出信息对话框:
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("First Window")
window.geometry("350x200")

def f01():
    messagebox.showinfo("Message title", "1--Message content")
btn1 = Button(window, text="Click here", command=f01)
btn1.grid(column=1, row=0)

def f02():
    messagebox.showinfo("Message title", "2--Message content")
btn2 = Button(window, text="Click here", command=f02)
btn2.grid(column=2, row=0)

def f03():
    messagebox.showinfo("Message title", "3--Message content")
btn3 = Button(window, text="Click here", command=f03)
btn3.grid(column=3, row=0)



window.mainloop()
