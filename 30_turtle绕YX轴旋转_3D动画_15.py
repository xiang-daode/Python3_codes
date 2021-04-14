import math
from turtle import *
import random as rnd

# 初始化:
setworldcoordinates(-600, -400, 600, 400)  # 设置坐标系
tracer(False)  # 快速(不用小乌龟)
ht()  # 隐藏小乌龟
pensize(1)  # 画笔粗细:1

L=[]
for t in range(0, 800,4):
    # 生成球面坐标点:
    x1 = t* math.cos(t / 17)
    y1 = t* math.sin(t / 17)
    z1 = t*(rnd.random()-0.5)
    L.append([x1,y1,z1])


def main(m,L):
        clear()
        for t in range(0, 200):
            x1=L[t][0]
            y1=L[t][1]
            z1=L[t][2]

            # 绕Y旋转:
            x2 = x1 * math.cos(m / 17) - z1 * math.sin(m / 17)
            y2 = y1
            z2 = x1 * math.sin(m / 17) + z1 * math.cos(m / 17)
            # 绕X旋转:
            x3 = x2
            y3 = y2 * math.cos(m / 37) - z2 * math.sin(m / 37)
            z3 = y2 * math.sin(m / 37) + z2 * math.cos(m / 37)
            # 配色,绘制:
            pencolor((x1 / 7) % 1, (y1 / 13) % 1, (z1 / 17) % 1)
            if t == 0:
                pu()
                goto(x3, y3)
            else:
                pd()
                goto(x3, y3)
                dot(20)  # 画球半径:10
        update()  # 更新画布
        m -= 1
        # 递归:
        while m > 0:
            ontimer(main(m,L), 50)

main(900,L)
