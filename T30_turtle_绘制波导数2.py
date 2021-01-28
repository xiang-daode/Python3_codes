# 绘制波
import math
from turtle import *

N = 25


def f(x):
    return x


def jumpto(x, y):
    penup()
    goto(x, y)


def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)


def coosys():
    line(-N, 0, N + 1, 0)
    line(0, -2.5, 0, 2.5)


def plot(fun, y, color):
    pencolor(color)

    jumpto(0, y)
    pendown()
    dot(5)
    for i in range(-N,N):
        yi = -2*i*math.exp(-i*i)
        goto(i, yi)
        dot(5)


def main():
    reset()
    setworldcoordinates(-25, -1, 25, 1)
    speed(0)
    hideturtle()
    coosys()
    plot(f, 0, "blue")
    return "Done!"


if __name__ == "__main__":
    main()
    mainloop()

