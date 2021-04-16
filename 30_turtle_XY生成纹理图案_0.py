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
            setx(x)
            sety(y)
            #dot(5,'#'+hex(0x10+x%0xEF)[2:]+hex(0x10+y%0xEF)[2:]+hex(0x10+(x^y)%0xEF)[2:])
            dot(5,'#'+hex(0x100000+(x*y//100+(x//13)^(y//17))%0xEFFFFF)[2:])
main(5)
