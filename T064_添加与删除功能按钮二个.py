# 在这里写上你的代码 :-)
import tkinter as tk

root = tk.Tk()

w = tk.Canvas(root, width =700, height = 500)
w.pack()

line1 = w.create_line(0, 350, 700, 350, fill = "yellow")
line2 = w.create_line(400, 0, 400, 500, fill = "red", dash = (4, 4))
rect1 = w.create_rectangle(50, 25, 150, 75, fill = "blue")

w.coords(line1, 0, 25, 700, 525)
w.itemconfig(rect1, fill = "red")
w.delete(line2)


tk.Button(root, text = "添加一个绿色的矩形", command = (lambda: w.create_rectangle(250, 75, 350, 475, fill = "#00FF44"))).pack()
tk.Button(root, text = "删除全部", command = (lambda x = "all" : w.delete(x))).pack()

root.mainloop()
