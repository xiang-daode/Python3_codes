# 使用turtle绘图:
from math import *;from time import *;from turtle import *
#图片尺寸:150*150像素,从画图软件中逐一取出坐标(x,y):
fly=[70,1,45,59,2,84,2,100,52,83,56,133,54,156,85,156,84,135,89,83,138,100,137,83,93,59,71,1]
bgcolor("#acf") #天空背景色
for t in range(0,3000,3):
        g=-t/20; poly1 = []
        sn=sin(g);  cs=cos(g);
        s = Shape("compound")
        for i in range(0,len(fly)-2,2):
            x1=fly[i]*cs-fly[i+1]*sn
            y1=fly[i]*sn+fly[i+1]*cs
            x2=fly[i+2]*cs-fly[i+3]*sn
            y2=fly[i+2]*sn+fly[i+3]*cs
            poly1.append([x1,y1])
            poly1.append([x2,y2])
        #更新画面:
        s.addcomponent(poly1, "#CCC", "#00C") #填充色,边框色
        register_shape("fly", s)
        shape("fly")
        # 暂停n秒，然后删除图像:
        sleep(0.01)


