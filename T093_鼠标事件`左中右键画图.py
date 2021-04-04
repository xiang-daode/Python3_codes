# 在这里写上你的代码 :-)

import tkinter as tk

root = tk.Tk()
w = tk.Canvas(root, width = 800, height = 600)
w.pack()

def paint(event):
        x1, y1 = (event.x - 3), (event.y - 3)
        x2, y2 = (event.x + 3), (event.y + 3)
        w.create_oval(x1, y1, x2, y2, fill = "red")
def paint2(event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        w.create_line(x1, y1, x2, y2, fill = "green")
        w.create_line(x1, y2, x2, y1, fill = "green")
def paint3(event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        w.create_rectangle(x1, y1, x2, y2, fill = "blue")


w.bind("<B1-Motion>", paint) #[左]键
w.bind("<B2-Motion>", paint2) #[中]键
w.bind("<B3-Motion>", paint3) #[右]键

tk.Label(root, text = "按住鼠标[左|中|右]键并移动，开始绘制你的理想蓝图吧……").pack(side = "bottom")

root.mainloop()
