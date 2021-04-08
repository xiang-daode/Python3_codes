# 在这里写上你的代码 :-)
import math
import time
from tkinter import *

# 使用tkinter绘图:
root =Tk()
canvas =Canvas(width=1200, height=800, bg='white')
canvas.pack()

# 方向与法线示意图:
'''   ^ p2
     /|\
      |
      |
p3    |    p4
o-----+-----o
      p1

'''

#==========================================================
for t in range(1200): #外层循环,总的点数
    for k1 in range(t,t-4,-1):#内层循环,流动过程所绘对象
        #p1点:
        x1=600*(1+math.cos(k1/32))
        y1=400*(1+math.sin(k1/48))

        #p2点:
        k2=k1+4
        x2=600*(1+math.cos(k2/32))
        y2=400*(1+math.sin(k2/48))

        #方向方位角fy,法向量方位角(ct1,ct2):
        fy=math.atan2(y2-y1,x2-x1)
        ct1=fy+math.pi/2
        ct2=fy-math.pi/2

        #p3点:
        x3=x1+120*math.cos(ct1)
        y3 = y1 + 120 * math.sin(ct1)

        #p4点:
        x4=x1+120*math.cos(ct2)
        y4 = y1 + 120 * math.sin(ct2)

        #主轴线段与轨迹线:
        canvas.create_line(x1, y1, x2, y2, fill='#330088', tag="pic_" + str(k1),width=8)
        canvas.create_line(x1, y1, x2, y2, fill='#d0d0d0',  width=2) #轨迹线,不擦除
        #两翼线段:
        canvas.create_line(x3, y3, x2, y2, fill='#339944', tag="pic_" + str(k1), width=4)
        canvas.create_line(x4, y4, x2, y2, fill='#339944', tag="pic_" + str(k1), width=4)

        #更新:
        canvas.update()

    # 暂停n秒，然后删除图像:
    time.sleep(0.01)
    for k1 in range(t,t-4,-1):
        canvas.delete("pic_"+str(k1))
#==========================================================

#canvas内部绘制文字:
canvas.create_text(100, 60, text='已经画完了!')

#tkinter内部输出文字:
text = Text(root, width=36, height=1)
text.tag_config("tag_1", backgroun="yellow", foreground="blue")
text.insert("insert", "   ---- 程序设计: 项道德 ,2021-05-08", "tag_1")
text.pack()

def fun4():
    canvas.create_text(160, 80, text='需要100全金币才可以再来一遍!')
    canvas.create_text(160, 100, text='重新运行本程序也可以再来一遍的!')

Button(root, text='再来一遍', command=fun4).pack()


root.mainloop()
