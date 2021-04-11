from turtle import *

pencolor(1, 0, 0)  # 笔色
pensize(2)  # 笔粗细
fillcolor(1, 0, 1)  # 填充颜色

begin_fill()  # 开始填充
for j in range(0, 360, 5):  # 范围:0--->360,每次加10
    fd(j/2)  # 向前走多少
    lt(180 - j // 30)  # 向左转多少角度
end_fill()  # 结束填充
