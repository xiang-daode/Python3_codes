# 在这里写上你的代码 :-)
import math
import time
from tkinter import *

# 使用tkinter绘图:
root =Tk()
canvas =Canvas(width=1200, height=800, bg='#6688ee')
canvas.pack()
PI=3.14159265

# 画图片式大背景,使用tkinter加载图片文件:
Image=PhotoImage(file = "img.png")
canvas.create_image(773, 421, image = Image )

#画远近之山脉:
points1 = []
points2 = []
for x in range(0,1200,7):
   points1.append(x);points1.append(280+50*math.cos(x/31)+150*math.cos(x/219));
   points2.append(x);points2.append(390+40*math.cos(x/27)+60*math.cos(x/217));
canvas.create_polygon(points1, outline='#111',fill='#4e4', width=2)
canvas.create_polygon(points2, outline='#111',fill='#393', width=2)

# 每次的移动:
for t in range(0,9000,3):
        g1=0.5*math.sin(t/33)+PI/2
        g2=math.sin(t/33)+PI/2-.75
        x0=t%1200
        y0=400
        #椭圆式地毯: 
        canvas.create_oval(x0-144, 690-54, x0+144, 690+54, outline='#888',fill='#448', tag="pic_sun")
        #================  人体各部位(起始)  =================
        canvas.create_line(x0, y0-10, x0, y0-40, fill='#000000', tag="pic_b2",width=22) #头
        canvas.create_line(x0, y0, x0, y0-10, fill='#303030', tag="pic_b2",width=10) #颈
        canvas.create_line(x0, y0, x0, y0+120, fill='#000000', tag="pic_b2",width=20)#上体
        #手L:
        x1=x0+100*(math.cos(g1))
        y1=y0+100*(math.sin(g1))
        x2=x1+80*(math.cos(g2))
        y2=y1+80*(math.sin(g2))
        #canvas.create_oval(x1-14, y1-14, x1+4, y1+4, fill='#FF44ee', tag="pic" + str(k2))
        canvas.create_line(x0-10, y0, x1, y1, fill='#000', tag="pic_a1",width=6)
        canvas.create_line(x1, y1, x2, y2, fill='#000', tag="pic_b1",width=6)
        #手R:
        g1=0.5*math.sin(-t/33)+PI/2
        g2=math.sin(-t/33)+PI/2-.75
        x1=x0+100*(math.cos(g1))
        y1=y0+100*(math.sin(g1))
        x2=x1+80*(math.cos(g2))
        y2=y1+80*(math.sin(g2))
        #canvas.create_oval(x1-14, y1-14, x1+4, y1+4, fill='#FF44ee', tag="pic" + str(k2))
        canvas.create_line(x0, y0, x1, y1, fill='#000', tag="pic_a2",width=6)
        canvas.create_line(x1, y1, x2, y2, fill='#000', tag="pic_b2",width=6)

        #下肢偏移:
        y0+=120
        #脚L:
        g1=0.5*math.sin(t/33)+PI/2
        g2=0.8*math.sin(t/33)+PI/2+.3
        x1=x0+100*(math.cos(g1))
        y1=y0+100*(math.sin(g1))
        x2=x1+80*(math.cos(g2))
        y2=y1+80*(math.sin(g2))
        #canvas.create_oval(x1-14, y1-14, x1+4, y1+4, fill='#FF44ee', tag="pic" + str(k2))
        canvas.create_line(x0, y0, x1, y1, fill='#404040', tag="pic_a3",width=16)
        canvas.create_line(x1, y1, x2, y2, fill='#404040', tag="pic_b3",width=12)
        canvas.create_line(x2, y2, x2+29, y2, fill='#804040', tag="pic_b3",width=4)
        #脚R:
        g1=0.5*math.sin(-t/33)+PI/2
        g2=0.8*math.sin(-t/33)+PI/2+.3
        x1=x0+100*(math.cos(g1))
        y1=y0+100*(math.sin(g1))
        x2=x1+80*(math.cos(g2))
        y2=y1+80*(math.sin(g2))        
        canvas.create_line(x0, y0, x1, y1, fill='#606060', tag="pic_a4",width=16)
        canvas.create_line(x1, y1, x2, y2, fill='#606060', tag="pic_b4",width=12)
        canvas.create_line(x2, y2, x2+29, y2, fill='#804040', tag="pic_b4",width=4)
        #================  人体各部位(结束)  =================
        

        # 更新画布: 
        canvas.update()
        # 暂停n秒:
        time.sleep(0.001)
        #然后删除运动之图像:
        canvas.delete("pic_a1")
        canvas.delete("pic_b1")
        canvas.delete("pic_a2")
        canvas.delete("pic_b2")
        canvas.delete("pic_a3")
        canvas.delete("pic_b3")
        canvas.delete("pic_a4")
        canvas.delete("pic_b4")
        canvas.delete("pic_sun")
root.mainloop()
