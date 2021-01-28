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
    width(2)
    pencolor('red')
    line(-0.9*N, 0, 0.9*N+1, 0)
    write("X", font=("Times", 18, "bold"))
    pencolor('blue')
    line(0, -1.75, 0, 1.75)
    write("Y", font=("Times", 18, "bold"))

def plot(fun, y, color):
    pencolor(color)
    width(4)
    jumpto(-N, 0)

    #dot(5)
    for i in range(-N,N,2):
        x=i/10.0
        pe = math.exp(x)
        ne = math.exp(-x)
        yc = (pe - ne)/(pe + ne)
        if i==-N:
            jumpto(i,yc)
            pendown()
        goto(i,yc)
        #dot(5)

def main():
    reset()
    setworldcoordinates(-N,-2, N+1, 2.1)
    speed(0)
    hideturtle()
    coosys()
    plot(f, 0, "purple")
    pu()
    goto(2,1.6)
    pd()
    write("出图完成", font=("Times", 18, "bold"))
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()

