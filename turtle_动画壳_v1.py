# 在这里写上你的代码 :-)
import turtle
import math

k=1

def myFun(x,y,m):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.lt(m/25) #旋转(角度制)
    turtle.fillcolor("#FFEE44")  #填充色
    turtle.begin_fill()  #开始填充
    turtle.circle(20+200/(2+m*m), steps=3)
    turtle.end_fill()    #结束填充


def Draw():
    turtle.ht() #隐藏乌龟
    turtle.tracer(False) #快速直接画
    global k
    #指定区间逐一画图:
    turtle.clear()
    for m in range(-350,350,3):
        x=m;y=100*math.cos(m/150)
        myFun(x,y,m)
    turtle.update()
    k+=1
    turtle.ontimer(Draw(), 50)

Draw()
