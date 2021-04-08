
from tkinter import *


root =Tk()
canvas =Canvas(width=800, height=600, bg='#DDEEFF')
canvas.pack()

# 使用tkinter加载图片文件:
p00=PhotoImage(file = "ball.png")
canvas.create_image(400, 300, image = p00 )

root.mainloop()
