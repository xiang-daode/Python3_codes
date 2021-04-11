from turtle import *

pencolor(1, 0, 0)  # 笔色
pensize(6)  # 笔粗细
fillcolor(1, 0, 1)  # 填充颜色

begin_fill()  # 开始填充
for j in range(0, 360, 30):  # 范围:0--->360,每次加30
    fd(200)  # 向前走多少
    lt(180 - 30)  # 向左转多少角度
end_fill()  # 结束填充
