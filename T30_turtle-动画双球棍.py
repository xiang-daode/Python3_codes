from turtle import *
import math


def main():
    q = 0
    tracer(False)
    ht()
    color(0.2, 0.5, 0)
    width(8)
    while q < 36000:
        clear()

        a = 3.1416 * q / 3600
        xc = 200 * math.cos(a)
        yc = 200 * math.sin(a)

        begin_fill()
        fillcolor(0.75, 0, 0)
        goto(-xc, -yc)
        circle(50)
        goto(xc, yc)
        circle(50)
        end_fill()
        update()
        q = q + 2


############## start the Main #################
main()
