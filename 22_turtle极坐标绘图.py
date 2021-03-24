import math
from turtle import *


def main():
    ht();
    g=0;y=0;

    tracer(False) #for fast

    while g<240:
        g=g+0.05
        mx=300*math.cos(g/2.7)*math.cos(g/9)
        my=300*math.sin(g/2.7)*math.cos(g/9)
        mz =300* math.sin(g / 9)
        zc=1234/(mz-1234)
        xc=mx*zc
        yc=my*zc
        pu()
        goto(xc,yc)
        pd()
        color(0.5 + 0.5 * math.cos(yc/100), 0.5 + 0.5 * math.cos(xc/200), 0.5 + 0.5 * math.sin(zc/150))
        dot(8)
        update()

if __name__ == '__main__':
    main()
    mainloop()
