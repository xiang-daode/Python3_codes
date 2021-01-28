import math
from turtle import *

def main():
    m=0;tracer(False)
    while m<120:
        clear()        
        width(5)
        m=m+.002
        m2=math.sin(m)/2
        goto(-200*math.cos(m2),-200*math.sin(m2))  
        goto(200*math.cos(m2),200*math.sin(m2))  
        goto(200*math.cos(1+m2),200*math.sin(1+m2))  
        update()
   
main() #<<<==============


