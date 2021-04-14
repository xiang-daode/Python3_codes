import math
from turtle import *
import random as rnd

# 初始化:
setworldcoordinates(-600, -400, 600, 400)  # 设置坐标系
tracer(False)  # 快速(不用小乌龟)
ht()  # 隐藏小乌龟
pensize(4)  # 画笔粗细:4


def main(m):
        r = 260
        clear()
        for t in range(0, 100):
            # 生成球面坐标点:
            x1 = rnd.randint(-280,280)
            y1 = rnd.randint(-280,280)
            z1 = rnd.randint(-280,280)

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
                #pd()
                goto(x3, y3)
                dot(10)  # 画球半径:10
        update()  # 更新画布
        m -= 1
        # 递归:
        while m > 0:
            ontimer(main(m), 50)


main(900)
