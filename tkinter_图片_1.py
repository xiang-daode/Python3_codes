# 在这里写上你的代码 :-)
from tkinter import *

# 使用tkinter绘图:
root =Tk()
canvas =Canvas(width=800, height=600, bg='white')
canvas.pack()
photo1 =PhotoImage(file = "O.png")
canvas.create_image(400, 300, image = photo1)


root.mainloop()
