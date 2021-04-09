# 在这里写上你的代码 :-)
from tkinter import *

# :
root =Tk()
canvas =Canvas(width=800, height=600, bg='white')
canvas.pack()

for u in range(0,600,50):
  canvas.create_oval(u-50,u-50,u+50,u+50,fill='#7788FF')

root.mainloop()
