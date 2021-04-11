# 在这里写上你的代码 :-)
from tkinter import *

window = Tk()
window.title("First Window")
window.geometry("350x400")

def fun01():
    print(spin.get())

spin = Spinbox(window, values=(0,2,4,6,8,10), width=5,command=fun01)
spin.grid(column=0, row=0)
window.mainloop()
