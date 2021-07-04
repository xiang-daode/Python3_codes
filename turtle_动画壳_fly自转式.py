# 在这里写上你的代码 :-)
from  math import *
from time import *
from tkinter import *

# 使用tkinter绘图:
root =Tk()
canvas =Canvas(width=1200, height=800, bg='#ACF')
canvas.pack()
PI=3.14159265
#图片尺寸:138*156像素,从画图软件中逐一取出坐标(x,y):
fly=[70,1,45,59,2,84,2,100,52,83,56,133,54,156,85,156,84,135,89,83,138,100,137,83,93,59,71,1]
x0=600;y0=400


# 每次的移动:
for t in range(0,3000,3):
        g=-t/100
        sn=sin(g)
        cs=cos(g)
        for i in range(0,len(fly)-2,2):
            x1=fly[i]*cs-fly[i+1]*sn
            y1=fly[i]*sn+fly[i+1]*cs
            x2=fly[i+2]*cs-fly[i+3]*sn
            y2=fly[i+2]*sn+fly[i+3]*cs
            canvas.create_line(x0+x1,y0+y1,x0+x2,y0+y2, fill='#FFF',tag="p"+str(i), width=6)
         #更新画面:
        canvas.update()
        # 暂停n秒，然后删除图像:
        sleep(0.001)
        for i in range(0,len(fly)-2,2):
            canvas.delete("p"+str(i));
root.mainloop()
