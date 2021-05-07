# 在这里写上你的代码 :-)
import turtle

def Trgl(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.lt(180) #旋转(角度制)
    turtle.fillcolor("#FF44EE")  #填充色
    turtle.begin_fill()  #开始填充
    turtle.circle(20, steps=3)
    turtle.end_fill()    #结束填充

def Draw():
    turtle.ht() #隐藏乌龟
    turtle.color("red")  #画笔颜色为红色
    turtle.tracer(False) #快速直接画

    #指定区间逐一画图:
    for x in range(-250,250,30):
        Trgl(x,0)

Draw()
