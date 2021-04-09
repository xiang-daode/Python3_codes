# 在这里写上你的代码 :-)
from tkinter import *

# 加载图片文件"O.png":
root =Tk()
canvas =Canvas(width=800, height=600, bg='white')
canvas.pack()
photo1 =PhotoImage(file = "O.png")

for u in range(-300,400,100):
  canvas.create_image(400+u, 300+u, image = photo1)


root.mainloop()
