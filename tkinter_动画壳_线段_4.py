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
        g1=0.5*math.sin(t/33)+PI/2
        g2=0.5*math.sin(t/33)+PI/2-.5
        x0=t%1200
        y0=400
        canvas.create_line(x0, y0-10, x0, y0-40, fill='#001100', tag="pic_b2",width=22) #头
        canvas.create_line(x0, y0, x0, y0-10, fill='#001100', tag="pic_b2",width=10) #颈
        canvas.create_line(x0, y0, x0, y0+120, fill='#001100', tag="pic_b2",width=20)#上体
        #手L:
        x1=x0+100*(math.cos(g1))
        y1=y0+100*(math.sin(g1))
        x2=x1+80*(math.cos(g2))
        y2=y1+80*(math.sin(g2))
        #canvas.create_oval(x1-14, y1-14, x1+4, y1+4, fill='#FF44ee', tag="pic" + str(k2))
        canvas.create_line(x0, y0, x1, y1, fill='#116600', tag="pic_a1",width=6)
        canvas.create_line(x1, y1, x2, y2, fill='#116600', tag="pic_b1",width=6)
        #手R:
        g1=0.5*math.sin(-t/33)+PI/2
        g2=0.5*math.sin(-t/33)+PI/2-.5
        x1=x0+100*(math.cos(g1))
        y1=y0+100*(math.sin(g1))
        x2=x1+80*(math.cos(g2))
        y2=y1+80*(math.sin(g2))
        #canvas.create_oval(x1-14, y1-14, x1+4, y1+4, fill='#FF44ee', tag="pic" + str(k2))
        canvas.create_line(x0, y0, x1, y1, fill='#110066', tag="pic_a2",width=6)
        canvas.create_line(x1, y1, x2, y2, fill='#110066', tag="pic_b2",width=6)


        y0+=120
        #脚L:
        g1=0.5*math.sin(t/33)+PI/2
        g2=0.5*math.sin(t/33)+PI/2+.2
        x1=x0+100*(math.cos(g1))
        y1=y0+100*(math.sin(g1))
        x2=x1+80*(math.cos(g2))
        y2=y1+80*(math.sin(g2))
        #canvas.create_oval(x1-14, y1-14, x1+4, y1+4, fill='#FF44ee', tag="pic" + str(k2))
        canvas.create_line(x0, y0, x1, y1, fill='#110066', tag="pic_a3",width=9)
        canvas.create_line(x1, y1, x2, y2, fill='#110066', tag="pic_b3",width=9)
        canvas.create_line(x2, y2, x2+29, y2, fill='#110066', tag="pic_b3",width=9)
        #脚R:
        g1=0.5*math.sin(-t/33)+PI/2
        g2=0.5*math.sin(-t/33)+PI/2+.2
        x1=x0+100*(math.cos(g1))
        y1=y0+100*(math.sin(g1))
        x2=x1+80*(math.cos(g2))
        y2=y1+80*(math.sin(g2))
        #canvas.create_oval(x1-14, y1-14, x1+4, y1+4, fill='#FF44ee', tag="pic" + str(k2))
        canvas.create_line(x0, y0, x1, y1, fill='#116600', tag="pic_a4",width=9)
        canvas.create_line(x1, y1, x2, y2, fill='#116600', tag="pic_b4",width=9)
        canvas.create_line(x2, y2, x2+29, y2, fill='#116600', tag="pic_b4",width=9)

        canvas.update()
        # 暂停n秒，然后删除图像:
        time.sleep(0.001)

        canvas.delete("pic_a1")
        canvas.delete("pic_b1")
        canvas.delete("pic_a2")
        canvas.delete("pic_b2")
        canvas.delete("pic_a3")
        canvas.delete("pic_b3")
        canvas.delete("pic_a4")
        canvas.delete("pic_b4")

root.mainloop()
