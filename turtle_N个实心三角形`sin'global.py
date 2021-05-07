# 在这里写上你的代码 :-)
import turtle

k=0

def Trgl(x,y):
    global k
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.lt(3) #旋转(角度制)
    turtle.fillcolor("#"+hex(0x100000+(k**9) % 0xEFFFFF)[2:])  #填充色
    turtle.begin_fill()  #开始填充
    turtle.circle(90-3*k, steps=3)
    turtle.end_fill()    #结束填充
    k+=1


def Draw():
    turtle.ht() #隐藏乌龟
    turtle.color("red")  #画笔颜色为红色
    turtle.tracer(False) #快速直接画

    #指定区间逐一画图:
    import math
    for x in range(-350,350,30):
        y=100*math.sin(x/200)
        Trgl(x,(int)(y))

Draw()
