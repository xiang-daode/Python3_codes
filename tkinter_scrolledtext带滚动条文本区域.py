# 在这里写上你的代码 :-)
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

window = Tk()
window.title("First Window")
window.geometry("780x620")

txt = scrolledtext.ScrolledText(window, width=108, height=40)
txt.grid(row=0)

def f01():
    txt.delete(1.0, END)
    txt.insert(INSERT, "************** \n"*800)

btn1 = Button(window, text="---------------f1---------------", command=f01)
btn1.grid( row=1,column=0)

def f02():
    txt.delete(1.0, END)
    txt.insert(INSERT, "============= \n"*800)

btn2 = Button(window, text="---------------f2---------------", command=f02)
btn2.grid(row=2,column=0)

def f03():
    messagebox.showinfo("title", "3-->{删除}")
    txt.delete(1.0, END)
btn3 = Button(window, text="---------------f3---------------", command=f03)
btn3.grid(row=3,column=0)


window.mainloop()
