import math
from turtle import *


def main():
    ht();
    x=0;y=0;
    
    tracer(False) #for fast

    while x<300:
        x=x+1
        mx=(x+50)*math.cos(x/35)
        my=(x+50)*math.sin(x/35)
        y=0
        while y<6.3:        
            #clear()
            dot(10)
            pu()        
            goto(mx+50*math.cos(y),my+50*math.sin(y))
            pd()          
            color(0.5+0.5*math.cos(y),0.5+0.5*math.cos(x),0.5+0.5*math.sin(3*y))
            dot(1)
            y=y+.2
            update()
     
     

if __name__ == '__main__':
    main()
    mainloop()


