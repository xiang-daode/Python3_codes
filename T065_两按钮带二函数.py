# 在这里写上你的代码 :-)

import tkinter as tk

root = tk.Tk()

w = tk.Canvas(root, width =700, height = 500)
w.pack()

def myDraw():
    w.create_line(0, 350, 700, 350, fill = "yellow")
    w.create_line(400, 0, 400, 500, fill = "red", dash = (4, 4))
    w.create_rectangle(50, 25, 150, 75, fill = "blue")
    w.create_rectangle(250, 75, 350, 475, fill = "#00FF44")
def myDel():
    #按序号逐一删除的用:
    #for i in range(5):
    #    w.delete(i)
    #删除全部的用:
    w.delete('all')

tk.Button(root, text = "添加图形", command = (lambda: myDraw())).pack()
tk.Button(root, text = "删除全部", command = (lambda : myDel())).pack()

root.mainloop()
