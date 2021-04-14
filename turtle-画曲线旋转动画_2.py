import math
from turtle import *


k=0
reset()
setworldcoordinates(-600,-400,600,400)#设置坐标系
tracer(False)
ht()
pensize(2)

def main(m):

    clear()
    for t in range(150):
        x1=t*math.cos(t/13)
        y1=t*math.sin(t/13)
        x2=x1*math.cos(m/17)-y1*math.sin(m/17)
        y2=x1*math.sin(m/17)+y1*math.cos(m/17)
        pencolor(math.exp(-t/100),0.5,math.exp(-t/100))
        goto(x2, y2)
        dot(16)
    update()
    m-=1
    while m>0:
      ontimer(main(m),50)

main(900)







