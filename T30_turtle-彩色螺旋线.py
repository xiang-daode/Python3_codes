import math
from turtle import *


def main():    
    x=0
    
    tracer(False) #for fast
    while x<12.56:        
        ht()
        bgcolor("gray20")        
        dot(10)
        pu()        
        goto((150+4*x)*math.cos(x),(150+4*x)*math.sin(x))
        pd()          
        color(0.5+0.5*math.cos(x),0.5+0.5*math.cos(5*x),0.5+0.5*math.sin(3*x))
        dot(25)
        x=x+0.05 
        update();
main()


