import math
from turtle import *


N = 100

def jumpto(x, y):
    penup()
    goto(x,y)

def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)

def coosys():    
    pencolor('red')   
    line(-1, 0, N+1, 0)
    line(0, -0.1, 0, 1.1)

def plot(color):
    pencolor(color) 
    jumpto(0,0.4)
    pendown()
    for i in range(N):
        yi=0.4+0.3*math.sin(i/2)*math.sin(i/20)
        goto(i,yi)
        

def main():
    reset()
    setworldcoordinates(-1.0,-0.1, N+1, 1.1)
    speed(0)
    hideturtle()
    width(4)
    coosys()
    plot("green")
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()

