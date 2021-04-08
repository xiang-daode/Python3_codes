# 在这里写上你的代码 :-)
import math
import time
from tkinter import *

# 使用tkinter绘图:
root =Tk()
canvas =Canvas(width=1200, height=800, bg='white')
canvas.pack()

# 每次的移动:
for t in range(1000):
    for k1 in range(t,t-8,-1):
        x1=600*(1+math.cos(k1/32))
        y1=400*(1+math.sin(k1/48))
        k2=k1-4
        x2=600*(1+math.cos(k2/32))
        y2=400*(1+math.sin(k2/48))
        canvas.create_oval(x1-14, y1-14, x1+4, y1+4, fill='#FF44ee', tag="pic" + str(k2))
        canvas.create_rectangle(x1-4, y1-4, x1+14, y1+14, fill='#3344ff',tag ="pic"+str(k1))
        canvas.create_line(x1, y1, x2, y2, fill='#33ffee', tag="pic_" + str(k1),width=9)
        canvas.update()
    # 暂停n秒，然后删除图像:
    time.sleep(0.001)
    for k1 in range(t,t-8,-1):
        canvas.delete("pic"+str(k1))

root.mainloop()
