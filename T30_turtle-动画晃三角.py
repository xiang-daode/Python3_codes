import math
from turtle import *

def main():
    m=0
    tracer(False)
    width(5);color(1,0,0)
    while m<320:
        clear()
        m=m+.002
        m2=math.sin(m)/2
        goto(0,0) 

        pd()
        goto(280*math.cos(m2),280*math.sin(m2));dot(22)  
        goto(320*math.cos(m2*1.6),320*math.sin(m2*1.6)) ;dot(22) 
        goto(0,0); dot(22)
        pu()
        
        update()    
main() #<<<==============


