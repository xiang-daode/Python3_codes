import math
from turtle import *


PI = 3.142

def jumpto(x, y):
    penup()
    goto(x,y)    
    
def line(x1, y1, x2, y2):
    jumpto(x1, y1);dot(15)
    pendown()
    goto(x2, y2);dot(15)
    penup()

def coosys():    
    pencolor('red');line(-1000, 0, 1000, 0);write("X",  font = ("Times", 18,"bold"))
    pencolor('green');line(0, -800, 0, 800);write("Y",  font = ("Times", 18,"bold"))

def plot(i):    
    for j in range(0,i+60,60):      
        xi=500+300*math.cos(PI*j/1800)+60*math.cos(PI*j/300)
        yi=100+100*math.sin(PI*j/1800)+20*math.sin(PI*j/300)
        if j==0:
            goto(xi,yi)
            pendown()
        goto(xi,yi);dot(5)
        update()
        
def   TwoLeg(xi,yi,i):
    clear()
    coosys()
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    L=500
    op=math.sqrt(xi**2+yi**2)
    fy=math.atan2(yi,xi)
    v=(2*L**2-xi**2-yi**2)/(2*L**2)
    af=math.acos(v)    
    ct=(math.pi-af)/2
    x1=L*math.cos(ct+fy)
    y1=L*math.sin(ct+fy)
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    width(8);line(0, 0, x1, y1);
    width(8);line(x1, y1, xi, yi);  
    goto(x1, y1);dot(25)
    goto(0, 0);dot(25)
    width(1);plot(i)
    

def main():
    reset()
    setworldcoordinates(-200,-100,1200,1000)#设置坐标系
    tracer(False)
    hideturtle()
    i=0
    while i<3600:
        xi=500+300*math.cos(PI*i/1800)+60*math.cos(PI*i/300)
        yi=100+100*math.sin(PI*i/1800)+20*math.sin(PI*i/300)
        TwoLeg(xi,yi,i)  
        i=i+30
    write("   完成一周",  font = ("Times", 18,"bold"))
    color(1,0,0);goto(200,800);write("二段式机械臂之逆解",  font = ("黑体", 24,"bold"))
    ontimer(main,1000)

if __name__ == "__main__":
    main()
    mainloop()

