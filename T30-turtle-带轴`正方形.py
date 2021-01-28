import math
from turtle import *


PI = 3.142

def jumpto(x, y):
    penup()
    goto(x,y)

def line2(x1, y1, x2, y2,color,w):
    width(w)
    pencolor(color)  
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)


def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2)    

def coosys():    
    pencolor('red')   
    line(-1000, 0, 1000, 0)
    line(0, -1000, 0, 1000)

L=[[-500,-500],
   [-500,500],
   [500,500],
   [500,-500],
   [-500,-500]]


def plot(color):
    pencolor(color) 
    jumpto(L[0][0],L[0][1])
    pendown()
    for i in range(len(L)):
        xi=L[i][0]
        yi=L[i][1]        
        goto(xi,yi)
        dot(8)
       

def main():
    reset()
    setworldcoordinates(-1200,-1000,1200,1000)
    speed(0);    hideturtle()
    width(1);    coosys()
    width(2);    plot("green")
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()

