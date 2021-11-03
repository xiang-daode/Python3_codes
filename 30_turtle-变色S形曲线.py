from turtle import *

# 变色S形曲线:
pensize(6)

for j in range(0,366,6):
    u=j/360
    pencolor(1-u,u/2,u)
    fd(25)
    lt((j-180)/10)





