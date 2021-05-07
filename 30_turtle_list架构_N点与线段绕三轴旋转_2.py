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
L = [] #装载三维点


# 三维的点,可以是箱子,也可以是大树,圆锥,房子,...等等
''' #=========立方体===========
L.append([s, s, s])
L.append([-s, s, s])
L.append([-s, -s, s])
L.append([s, -s, s])
L.append([s, -s, -s])
L.append([-s, -s, -s])
L.append([-s, s, -s])
L.append([s, s, -s])
L.append([s, s, s])

#===== 锥面曲线 =======
for g in range(0,360,1):
    q=3.1416*g/180
    x=g*math.cos(q *13)/5
    y=g*math.sin(q *13)/5
    z=g/2
    L.append([x,y,z-390])

'''
#===== 球面曲线 =======
for g in range(0,360,1):
    q=3.1416*g/180
    x=s*math.cos(q *13)*math.cos(q * 3)
    y=s*math.sin(q *13)*math.cos(q * 3)
    z=s*math.sin(q * 3)
    L.append([x,y,z])




#=================================

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
        y3 = y2 * math.cos(m / 47) - z2 * math.sin(m / 47)
        z3 = y2 * math.sin(m / 47) + z2 * math.cos(m / 47)

        # 配色,绘制:
        far=(z3+250)/500
        pencolor(far, far, far)

        if t == 0:
            pu()
            goto(x3, y3)
        else:
            pensize(8-8*far) #线段粗细
            pd()
            goto(x3, y3)
            dot(12-8*far)  # 画球半径
    update()  # 更新画布
    m -= 1
    # 递归:
    if m > 0:
        ontimer(main(m, L), 20)

main(300, L)
