from turtle import *
import math

def main():    
    tracer(False);ht()
 
    while True:
        for q in range(1,36000,1):            
            clear()
            a=3.1416*q/18000
            xc=300*math.cos(a)
            yc=300*math.sin(a)
            goto(xc,yc-50)         
            circle(50)                    
            update()            
    return "DONE!"

############## start the Main #################
main()


