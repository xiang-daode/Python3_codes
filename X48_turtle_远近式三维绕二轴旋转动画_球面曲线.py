import math;from turtle import *
#初始化:
setworldcoordinates(-600,-400,600,400)#设置坐标系
tracer(False) #快速(不用小乌龟)
ht() #隐藏小乌龟
pensize(4)#画笔粗细:4
#自编主函数：
def main(m):
    r=240; clear()
    for t in range(360):
        #生成球面坐标点:
        x1=r*math.cos(t/7)*math.cos(t/29)
        y1=r*math.sin(t/7)*math.cos(t/29)
        z1=r*math.sin(t/29)
        #绕Y旋转:
        x2=x1*math.cos(m/17)-z1*math.sin(m/17)
        y2=y1
        z2=x1*math.sin(m/17)+z1*math.cos(m/17)
        #绕X旋转:
        x3=x2
        y3=y2*math.cos(m/37)-z2*math.sin(m/37)
        z3=y2*math.sin(m/37)+z2*math.cos(m/37)
        #配色,绘制:
        pencolor((x1/17)%1,(y1/17)%1,(z1/17)%1)
        pensize((z3+r)/90)
        if z3<0:
            pencolor(.9,.9,.9); pensize(0)
        if t==0:
            pu();  goto(x3, y3)
        else:
            pd();  goto(x3, y3); #dot((z3+r)/30) #画球半径
    m-=1;update() #更新画布

    #递归:
    while m>0:
      ontimer(main(m),5)
main(900) #运行主函数







