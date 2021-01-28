import math
from turtle import *


PI = 3.142

def jumpto(x, y):
    penup()
    goto(x,y)

def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)

def coosys():    
    pencolor('red')   
    line(-1000, 0, 1000, 0)
    line(0, -1000, 0, 1000)

def plot(color):
    pencolor(color) 
    jumpto(0,0)
    pendown()
    for i in range(360):
        xi=i*(math.cos(PI*i/90))
        yi=i*(math.sin(PI*i/90))
        goto(xi,yi)
        

def main():
    reset()
    setworldcoordinates(-1200,-1000,1200,1000)
    speed(0);    hideturtle()
    width(2);    coosys()
    width(5);    plot("green")
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()

