import math
from turtle import *

m=50
def main(m):    
    x=0    
    clear();width(9);ht()
    tracer(False)   #for fast
    m2=50*math.cos(m/13)
    m=m+.1      
    while x<4*6.3:        
        fillcolor(0.5+0.5*math.cos(x),0.5+0.5*math.cos(x+m2),0.5+0.5*math.cos(m2))
        begin_fill()     
        goto((50+8*x)*math.cos(m2+x-0.5),(50+8*x)*math.sin(m2+x-0.5))
        end_fill()
        x=x+0.05 
        update();    
    
    return main(m)    
main(m)


