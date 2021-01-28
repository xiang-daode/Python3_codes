from turtle import *
import math

def main():
    
    ht()
    while True:
        for q in range(0,36000,1):
            clear();  tracer(False)
            a=3.1416*q/18000
            xc=300*math.cos(a)
            yc=300*math.sin(a)
            goto(xc,yc)
            dot(25)            
            update()            
    return "DONE!"

############## start the Main #################
main()


