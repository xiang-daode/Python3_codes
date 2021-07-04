# 使用turtle绘图:
from  math import *;from time import *;from  turtle import *;

#图片尺寸:138*156像素,从画图软件中逐一取出坐标(x,y):
fly=[70,1,45,59,2,84,2,100,52,83,56,133,54,156,85,156,84,135,89,83,138,100,137,83,93,59,70,1]
bgcolor("#acf") #天空,背景色
# 动画的移动控制t:
for t in range(0,3000,3):
        g=-t/20;u=1.25+sin(t/120)
        sn=u*sin(g) #三角函数:正弦
        cs=u*cos(g) #三角函数:余弦
        s = Shape("compound")
        poly1 = [] #list
        for i in range(0,len(fly)-2,2): #二维旋转计算(x1,y1),(x2,y2)
            x1=fly[i]*cs-fly[i+1]*sn
            y1=fly[i]*sn+fly[i+1]*cs
            x2=fly[i+2]*cs-fly[i+3]*sn
            y2=fly[i+2]*sn+fly[i+3]*cs
            poly1.append([x1,y1])
            poly1.append([x2,y2])
        #更新画面:
        s.addcomponent(poly1, "#FFF", "#F88") #填充色,边框色
        register_shape("myshape", s)
        shape("myshape")
        # 暂停n秒:
        sleep(0.01)


