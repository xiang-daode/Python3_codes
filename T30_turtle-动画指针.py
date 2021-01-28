import math
from turtle import *

def main():
    m=0
    while m<330:
        clear()
        tracer(False)
        width(5)
        m=m+.001
        m2=math.sin(m)/2
        goto(0,0)
        goto(300*math.cos(m2),300*math.sin(m2))  
        update()
main() #<<<==============


