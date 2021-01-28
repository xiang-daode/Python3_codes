from turtle import *
import math

def main():
    tracer(False);ht()
    width(1)
    while True:
        for q in range(1,36000,5):
            bgcolor(0,0,0.2)
            clear()
            a=3.1416*q/18000
            xc=300*math.cos(a)
            yc=300*math.sin(a)
            pencolor(0.5+0.5*math.cos(a-2),0.5+0.5*math.cos(a-3),0.5+0.5*math.cos(a-4))
            begin_fill()
            fillcolor(0.5+0.5*math.cos(a-1),0.5+0.5*math.cos(a),0.5+0.5*math.cos(a+1))
            goto(xc,yc-50)
            circle(50,180)
            goto(25+xc,yc+50)
            circle(50,-180)
            end_fill()
            update()

    return "DONE!"

############## start the Main #################
main()


