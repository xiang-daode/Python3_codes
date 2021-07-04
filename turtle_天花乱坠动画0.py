from turtle import *
from math import *


w=-600
tracer(False) #快速直接画
ht() #隐藏乌龟

def main():
    global w
    #clear()
    goto(w,0)
    goto(w,w%50)
    w+=1
    update()
    ontimer(main(),10)

main()

