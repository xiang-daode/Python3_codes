import math
from turtle import *

PI = 3.142

# 跳到指定坐标:
def jumpto(x, y):
    penup()
    goto(x, y)

# 在两点之间画线段:
def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)

# 绘制坐标轴:
def coosys():
    pencolor('red')
    line(-1000, 0, 1000, 0)
    write("X", font=("Times", 18, "bold"))  # 输出文本
    line(0, -1000, 0, 1000)
    write("Y", font=("Times", 18, "bold"))  # 输出文本

# 绘图主函数:
def plot(color):
    pencolor(color)
    num=6  #七叶

    # 在极坐标系下绘图:
    for i in range(0,365,5):
        if i==0:
            xi = 500 * math.cos(PI * i / 180) + 250 * math.sin(6 * PI * i / 180)
            yi = 500 * math.sin(PI * i / 180) + 250 * math.cos(6 * PI * i / 180)
            jumpto(xi,yi)
            pendown()

            begin_fill()
        xi = 500 * math.cos(PI * i / 180) + 250 * math.sin(num*PI * i / 180)
        yi = 500 * math.sin(PI * i / 180) + 250 * math.cos(num*PI * i / 180)
        goto(xi, yi)
    end_fill()

    # 在直角坐标系下绘图:
    pencolor('purple')
    for i in range(-1000,1001,10):
        x=i/100.0
        pe = math.exp(x)
        ne = math.exp(-x)
        yc = 200*(pe - ne)/(pe + ne)
        if i==-1000:
            jumpto(i,yc)
            pendown()
        goto(i,yc)

def main():
    reset()
    setworldcoordinates(-1200, -1000, 1200, 1000) #定制坐标系范围
    speed(0);
    hideturtle()
    width(2);
    coosys()
    width(5);
    bgcolor("yellow")
    color("green","green")
    plot("green")
    pencolor('pink')
    write("出图完成", font=("Times", 18, "bold")) # 输出文本
    return "Done!"


if __name__ == "__main__":
    main()
    mainloop()

