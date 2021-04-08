# 在这里写上你的代码 :-)
import math
import time
from tkinter import *
import random as rnd

# 使用tkinter绘图:
root =Tk()
canvas =Canvas(width=1200, height=800, bg='white')
canvas.pack()
photo1 =PhotoImage(file = "Q.png")


for t in range(1000):# 总循环多少次
    for k in range(10):# 每次生成多少个
        xt=rnd.randint(100,1100)
        yt=rnd.randint(100,700)
        canvas.create_image(xt, yt, image = photo1,tag ="pic"+str(k))
        canvas.update()
    # 暂停n秒，然后删除图像:
    time.sleep(0.1)
    for k in range(10):
        canvas.delete("pic"+str(k))

root.mainloop()
