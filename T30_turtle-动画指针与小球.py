from turtle import *
import math

def main():
    
    ht()
    while True:
        for q in range(10,1800,1):
            bgcolor(1,1,1)
            clear(); tracer(False)
            a=3.1416*q/1800
            xc=300*math.cos(a)
            yc=300*math.sin(a)
            width(5);color(0,0,0.5)
            goto(0,0)
            goto(xc,yc)
            dot(45)           
            update()
        for q in range(1800,3600,1):
            clear();  tracer(False)
            a=3.1416*q/1800
            xc=300*math.cos(-a)
            yc=300*math.sin(-a)
            width(5);color(0,0.5,0)
            pu()
            goto(0,0)
            goto(xc,yc)
            pd()
            dot(65)
            
            update()
            
    return "DONE!"

############## start the Main #################
main()


