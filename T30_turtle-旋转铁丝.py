import math
from turtle import *

m=50
def main(m):    
    x=0    
    clear()
    tracer(False)   #for fast
    m2=50*math.cos(m/13)
    while x<6.3:        
        ht()
        width(5)
        goto((150+14*x)*math.cos(m2+x),(150+14*x)*math.sin(m2+x))
        x=x+0.05 
        update();
    m=m+.03    
    return main(m)    
main(m)


