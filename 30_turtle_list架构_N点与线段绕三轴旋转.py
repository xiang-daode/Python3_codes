import sys
import math
from turtle import *
import random as rnd

sys.setrecursionlimit(3000)

# 初始化:
setworldcoordinates(-600, -400, 600, 400)  # 设置坐标系
tracer(False)  # 快速(不用小乌龟)
ht()  # 隐藏小乌龟
pensize(20)  # 画笔粗细
u = 0.9  # 衰减因子

# Y+对向天,Z+对向人:
s = 250
L = []
# 三维的点,可以是箱子,也可以是大树,圆锥,房子,...等等
L.append([s, s, s])
L.append([-s, s, s])
L.append([-s, -s, s])
L.append([s, -s, s])
L.append([s, -s, -s])
L.append([-s, -s, -s])
L.append([-s, s, -s])
L.append([s, s, -s])
L.append([s, s, s])

def main(m, L):
    clear()
    for t in range(len(L)):
        x0 = L[t][0]
        y0 = L[t][1]
        z0 = L[t][2]

        # 绕Z旋转:
        x1 = x0 * math.cos(m / 97) - y0 * math.sin(m / 97)
        y1 = x0 * math.sin(m / 97) + y0 * math.cos(m / 97)
        z1 = z0

        # 绕Y旋转:
        x2 = x1 * math.cos(m / 37) + z1 * math.sin(m / 37)
        y2 = y1
        z2 = -x1 * math.sin(m / 37) + z1 * math.cos(m / 37)

        # 绕X旋转:
        x3 = x2
        y3 = y2 * math.cos(-0.15) - z2 * math.sin(-0.15)
        z3 = y2 * math.sin(-0.15) + z2 * math.cos(-0.15)

        # 配色,绘制:
        pencolor((x1 / 7) % 1, (y1 / 13) % 1, (z1 / 17) % 1)

        if t == 0:
            pu()
            goto(x3, y3)
        else:
            pensize(8) #线段粗细
            pd()
            goto(x3, y3)
            dot(25)  # 画球半径
    update()  # 更新画布
    m -= 0.1
    # 递归:
    if m > 0:
        ontimer(main(m, L), 20)

main(300, L)
