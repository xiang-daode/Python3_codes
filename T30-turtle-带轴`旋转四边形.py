import math
from turtle import *


PI = 3.14159265

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
   [-500,300],
   [300,300],
   [300,-500],
   [-500,-500]]


def plot(color):
    pencolor(color)
    pendown()
    for q in range(0,360,12):   
        for i in range(len(L)):
            xi=L[i][0]*math.cos(q*PI/180)- L[i][1]*math.sin(q*PI/180) 
            yi=L[i][0]*math.sin(q*PI/180)+ L[i][1]*math.cos(q*PI/180)        
            if i==0:
                jumpto(xi,yi);pendown()
            dot(8)
            goto(xi,yi)
       

def main():
    reset()
    setworldcoordinates(-1200,-1000,1200,1000)
    speed(0);    hideturtle()
    width(5);    coosys()
    width(2);    plot("green")
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()

