#!/usr/bin/python
# -*- coding: cp936 -*-

#!/usr/bin/env python3

from turtle import *

def yin(radius, color1, color2):
    width(3)
    color("red", color1)

    begin_fill()
    circle(-radius, 360)
    left(180)
    circle(1.5*radius, 360)
    end_fill()    

def main():
    reset()
    yin(80, "yellow", "white")    
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()




