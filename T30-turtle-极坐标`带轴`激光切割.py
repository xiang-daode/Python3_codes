#引用,导入海龟库与数学库:
from turtle import *
from numpy import *  

PI = 3.142 

#跳到指定点:
def jumpto(x, y):
    penup()
    goto(x,y)

#画线段:
def line(x1, y1, x2, y2):
    jumpto(x1, y1)
    pendown()
    goto(x2, y2);penup()

#坐标系二轴线:
def coosys():    
    pencolor('red')   
    line(-1000, 0, 1000, 0);write("X",  font = ("黑体", 16,"bold"))
    pencolor('green') 
    line(0, -800, 0, 800);write("Y",  font = ("黑体", 16,"bold"))

#插补与绘图:
def plot():
    bgcolor(0,0,0)

    #圆:
    jumpto(0,-200);pencolor(1,1,0.5)
    pd();circle(200); pu() 

    #圆角正方形:
    R=300000;pencolor(0.5,1,1)
    for i in range(45,360+90,5):
        if i==45:
            xi=R*math.cos(PI*i/180)
            yi=R*math.sin(PI*i/180)
            goto(sign(xi)*(abs(xi)**.5),sign(yi)*(abs(yi)**.5))  
        pendown()  
        xi=R*math.cos(PI*i/180)
        yi=R*math.sin(PI*i/180)
        goto(sign(xi)*(abs(xi)**.5),sign(yi)*(abs(yi)**.5))

    #星形线:
    R=5;pu();pencolor(1,0.5,1)
    for i in range(45,360+90,5):
        if i==45:
            xi=R*math.cos(PI*i/180)
            yi=R*math.sin(PI*i/180)
            goto(sign(xi)*(abs(xi)**4),sign(yi)*(abs(yi)**4))  
        pendown()  
        xi=R*math.cos(PI*i/180)
        yi=R*math.sin(PI*i/180)
        goto(sign(xi)*(abs(xi)**4),sign(yi)*(abs(yi)**4))

#主程序:
def main():
    reset()
    setworldcoordinates(-1200,-1000,1200,1000)
    speed(8);    hideturtle()
    width(2);    coosys()
    width(4);    plot()
    
    return "Done!"

#主程序启动循环:
if __name__ == "__main__":
    main()
    mainloop()

