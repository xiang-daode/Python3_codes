# 在这里写上你的代码 :-)
import math
import time
from tkinter import *

# 使用tkinter绘图:
root =Tk()
canvas =Canvas(width=1200, height=800, bg='white')
canvas.pack()
PI=3.14159265
# 每次的移动:
for t in range(0,3000,3):
        g1=math.sin(t/33)+PI/2
        g2=1.7*math.sin(t/33)+PI/2
        x0=600
        y0=400

        x1=x0+130*(math.cos(g1))
        y1=y0+130*(math.sin(g1))
        x2=x1+110*(math.cos(g2))
        y2=y1+110*(math.sin(g2))

        canvas.create_line(x0, y0, x1, y1, fill='#110066', tag="pic_a1",width=12)
        canvas.create_line(x1, y1, x2, y2, fill='#110066', tag="pic_b1",width=6)
        canvas.create_oval(x0-14, y0-14, x0+14, y0+14, fill='#FF44ee', tag="pic0")
        canvas.create_oval(x1-14, y1-14, x1+14, y1+14, fill='#44ee66', tag="pic1")
        canvas.create_oval(x2-24, y2-24, x2+24, y2+24, fill='#112233', tag="pic2")
        canvas.update()
        # 暂停n秒，然后删除图像:
        time.sleep(0.001)
        canvas.delete("pic0");canvas.delete("pic1");canvas.delete("pic2")
        canvas.delete("pic_a1")
        canvas.delete("pic_b1")


root.mainloop()
