# 打开文件对话框:
from tkinter import *
from tkinter import filedialog
import os

window = Tk()
window.title("First Window")
window.geometry('1200x600')
def clicked():
    file = filedialog.askopenfilenames(initialdir=os.path.dirname(__file__))
    print(file[0]) #可以是多个文件的

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=0, row=0)

window.mainloop()
