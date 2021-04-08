# 在这里写上你的代码 :-)
import math
import time
from tkinter import *

# 使用tkinter绘图:
root =Tk()
canvas =Canvas(width=1200, height=800, bg='white')
canvas.pack()
photo1 =PhotoImage(file = "O.png")

# 每次的移动:
for t in range(1000):
    for k in range(t,t-2,-1):
        xt=600*(1+math.cos(k/36)*math.cos(k/9))
        yt=400*(1+math.sin(k/36)*math.cos(k/9))
        canvas.create_image(xt, yt, image = photo1,tag ="pic"+str(k))
        canvas.create_oval(xt-15, yt-15, xt+15, yt+15, fill='#3344ee')
        canvas.update()
    # 暂停n秒，然后删除图像:
    time.sleep(0.001)
    for k in range(t,t-2,-1):
        canvas.delete("pic"+str(k))

root.mainloop()
