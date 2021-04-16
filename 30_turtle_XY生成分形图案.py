import sys
import math
from turtle import *
import random as rnd

sys.setrecursionlimit(3000)

# 初始化:
setworldcoordinates(-500, -500, 500, 500)  # 设置坐标系
tracer(False)  # 快速(不用小乌龟)
ht()  # 隐藏小乌龟

def main(N):
    for x in range(-500,500,5):
        for y in range(-500,500,5):
            xc,yc=x/300,y/300
            xx,yy=xc,yc
            for k in range(N):
                xx=xc*xc-yc*yc+0.425
                yy=2*xc*yc+0.525
                if xx*xx+yy*yy>2:
                    break;
                else:
                    xc,yc=xx,yy
            pencolor(0.5+0.5*math.cos(xc),0.5+0.5*math.sin(3*xx),0.5-0.5*math.cos(7*yc))
            setx(x)
            sety(y)
            dot(5)
            k+=1
main(5)
