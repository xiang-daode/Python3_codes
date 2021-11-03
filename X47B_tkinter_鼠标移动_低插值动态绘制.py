# 线段飞机
import time
import tkinter as tk
import math

root = tk.Tk();w = tk.Canvas(root, width = 1000, height = 700);w.pack()
lmd=2  #每一线段细分数目
rt=5 #飞机缩小倍数,取原始大小的1/5
#在100x100像素中画图(头向上),沿一周依次记下转弯点的坐标:
P=[50,0,41,33,0,63,0,71,41,65,40,86,32,92,32,100,67,100,67,92,59,86,58,65,99,71,100,63,60,34,50,0]

#飞机飞行函数:
def myMV(angle,xc,yc):
        w.delete('oval'); w.delete('poly1')
        cos=math.cos(angle+math.pi/2); #余弦函数
        sin=math.sin(angle+math.pi/2); #正弦函数
        Q=[] #记录飞机平移旋转后的新坐标
        for i in range(0,(int)(len(P)/2),1): #处理平移与二维旋转
            xi=P[2*i]-50
            yi=P[2*i+1]-50
            xx=xc+(xi*cos-yi*sin)/5
            yy=yc+(xi*sin+yi*cos)/5
            Q.append(xx) ;Q.append(yy)
        w.create_polygon(Q,outline='black', fill='#CDE', tag='poly1')#实心的多边形
        w.create_line(xc ,yc, xc+xx/200, yc+yy/200, fill="#AAA",dash=(1, 12),width=12)#留下烟尾
        w.update()

tk.Label(root, text = "程序控制无人机",font=('simhei',24,''),foreground='#909').pack()
tk.Label(root, text = "程序设计:项道德,于2021-08-12",font=('simhei',16,''),foreground='#090').pack(side = "bottom")
#读取飞行航线数据:
with open("data.txt","r") as fr:
    txt=fr.read()
    s0=txt.split('\n')
    s1=s0[slice(len(s0)-1)]
    #print(s1)
    k=0
    for m in s1:
        if k==0:
            x0=int(m.split(',')[0])
            y0=int(m.split(',')[1])
        else:
            xc=int(m.split(',')[0])
            yc=int(m.split(',')[1])
            angle=math.atan2(yc-y0,xc-x0) #反正切函数,计算出前进方向的航向角度
            for d in range(lmd):
                myMV(angle,x0 +d*(xc-x0)/lmd,y0+d*(yc-y0)/lmd)
                time.sleep(.01)
            x0=xc;y0=yc
        k=k+1
    #回家阶段:
    k=0
    for m in ['1000,450','600,580','300,600','100,600']:
        if k==0:
            x0=int(m.split(',')[0])
            y0=int(m.split(',')[1])
        else:
            xc=int(m.split(',')[0])
            yc=int(m.split(',')[1])
            angle=math.atan2(yc-y0,xc-x0) #反正切函数,计算出前进方向的航向角度
            for d in range(lmd):
                myMV(angle,x0 +d*(xc-x0)/lmd,y0+d*(yc-y0)/lmd)
                #time.sleep(.01)
            x0=xc;y0=yc
        k=k+1

root.mainloop()


