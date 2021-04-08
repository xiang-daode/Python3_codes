# 在这里写上你的代码 :-)
import math
import time
from tkinter import *

# 使用tkinter绘图:
root =Tk()
canvas =Canvas(width=900, height=700, bg='white')
canvas.pack()
photo1 =PhotoImage(file = "ball.png")

# 每次的移动:
for t in range(1000):
    xt=400*(1+math.cos(t/23))
    yt=300*(1+math.sin(t/19))
    canvas.create_image(xt, yt, image = photo1,tag ="pic")
    canvas.update()
    # 暂停n秒，然后删除图像:
    time.sleep(0.001)
    canvas.delete("pic")

root.mainloop()
