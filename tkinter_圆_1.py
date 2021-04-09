# 画一个圆:
from tkinter import *


root =Tk()
canvas =Canvas(width=800, height=600, bg='white')
canvas.pack()

canvas.create_oval(
400-100,300-100,400+100,300+100,
fill='#7788FF')

root.mainloop()
