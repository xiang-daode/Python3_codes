import sys
import math
from turtle import *
import random as rnd

sys.setrecursionlimit(3000)

# 初始化:
setworldcoordinates(-600, -400, 600, 400)  # 设置坐标系
tracer(False)  # 快速(不用小乌龟)
ht()  # 隐藏小乌龟
pensize(12)  # 画笔粗细:12
u=0.5 #衰减因子

#Y+对向天,Z+对向人:
x1,y1,z1,x2,y2,z2=0,0,0, 0,200,0
L=[]
L.append([x1,y1,z1])
L.append([x2,y2,z2])
def tree(x1,y1,z1,x2,y2,z2,L):
    h=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2-z1)*(z2-z1))
    print(len(L),sep=',')
    while h>45 and len(L)<200:
       if len(L)>3:
           k=rnd.randint(1,len(L)-1)
           x1,y1,z1=L[k-1][0],L[k-1][1],L[k-1][2]
           x2,y2,z2=L[k][0],L[k][1],L[k][2]
       h=math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2-z1)*(z2-z1))
       q1=(2*rnd.random()-1)+3.1416/2;q2=(2*rnd.random()-1)
       r=u*h
       x4,y4,z4=x2+r*math.cos(q1)*math.cos(q2),y2+r*math.sin(q1)*math.cos(q2),z2+r*math.sin(q2)
       L.append([x4,y4,z4])
       tree(x2,y2,z2,x4,y4,z4,L)


def main(m,L):
        clear()
        for t in range(len(L)):
            x1=L[t][0]
            y1=L[t][1]-300
            z1=L[t][2]

            # 绕Y旋转:
            x2 = x1 * math.cos(m / 17) - z1 * math.sin(m / 17)
            y2 = y1
            z2 = x1 * math.sin(m / 17) + z1 * math.cos(m / 17)
            # 绕X旋转:
            x3 = x2
            y3 = y2 *math.cos(-.137) - z2 * math.sin(-.137)
            z3 = y2 *math.sin(-.137) + z2 * math.cos(-.137)
            # 配色,绘制:
            pencolor((x1 / 7) % 1, (y1 / 13) % 1, (z1 / 17) % 1)
            if t == 0:
                pu()
                goto(x3, y3)
            else:
                pd()
                pensize(36/t)
                goto(x3, y3)
                dot(t/8)  # 画球半径
        update()  # 更新画布
        m -= 1
        # 递归:
        while m > 0:
            ontimer(main(m,L), 50)

tree(x1,y1,z1,x2,y2,z2,L)
main(3000,L)
