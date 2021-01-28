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
    line(-1, 0, N+1, 0)
    line(0, -0.1, 0, 1.1)

def plot(fun, y, color):
    pencolor(color)
    
    jumpto(0, y)
    pendown()
    dot(5)
    for i in range(N):
        yi=0.25+0.25*math.cos(i/10)
        goto(i,yi)
        dot(5)

def main():
    reset()
    setworldcoordinates(-1.0,-0.1, 101, 1.1)
    speed(0)
    hideturtle()
    coosys()
    plot(f, 0, "blue")
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()

