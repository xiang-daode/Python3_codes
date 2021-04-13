# 在这里写上你的代码 :-)
from tkinter import *

# 建立画布:
root =Tk()
canvas =Canvas(width=800, height=600, bg='white')
canvas.pack()

#画一些圆(椭圆)
for u in range(0,600,50):
  canvas.create_oval(u-60,u-40,u+60,u+40,fill='#7788FF')

root.mainloop()
