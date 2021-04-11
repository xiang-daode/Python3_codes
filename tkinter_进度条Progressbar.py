# 在这里写上你的代码 :-)
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
window = Tk()
window.title("First Window")
window.geometry('350x200')
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='#447799')
bar = Progressbar(window, length=350, style='black.Horizontal.TProgressbar')
bar['value'] = 70 #百分比
bar.grid(column=0, row=0)
window.mainloop()
