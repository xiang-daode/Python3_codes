import math
from turtle import *


N = 100

def f(x):
    return x

def jumpto(x, y):
    penup()
    goto(x,y)

def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)

def coosys():
    width(4)
    pencolor('red')
    line(-N, 0, N+1, 0)
    pencolor('blue')
    line(0, -2, 0, 2.1)

def plot(fun, y, color):
    pencolor(color)
    width(2)
    jumpto(-N, 0)
    pendown()
    #dot(5)
    for i in range(-N,N,2):
        yi=math.cos(i/10)
        goto(i,yi)
        #dot(5)

def main():
    reset()
    setworldcoordinates(-100,-2, 101, 2.1)
    speed(0)
    hideturtle()
    coosys()
    plot(f, 0, "green")
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()

