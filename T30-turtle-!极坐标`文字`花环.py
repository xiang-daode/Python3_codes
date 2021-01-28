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
    penup()

def coosys():    
    pencolor('red');line(-1000, 0, 1000, 0);write("X",  font = ("Times", 18,"bold"))
    pencolor('green');line(0, -800, 0, 800);write("Y",  font = ("Times", 18,"bold"))

def plot(color):
    pencolor(color) 
    for i in range(361):
        if i==0:
            xi=500*math.cos(PI*i/180)+60*math.sin(PI*i/10)
            yi=500*math.sin(PI*i/180)+60*math.cos(PI*i/10)
            goto(xi,yi)            
        pendown()
        xi=500*math.cos(PI*i/180)+60*math.sin(PI*i/10)
        yi=500*math.sin(PI*i/180)+60*math.cos(PI*i/10)
        goto(xi,yi)
        

def main():
    reset()
    setworldcoordinates(-1200,-1000,1200,1000)
    speed(0);    hideturtle()
    width(6);    coosys()
    width(3);    plot("blue")

    write("完成",  font = ("Times", 18,"bold"))
    return "Done!"

if __name__ == "__main__":
    main()
    mainloop()

