from turtle import *
import math

def main(): 
   pu()
   goto(-400,-200)
   #螺旋线:
   pd();width(5);pencolor(1,0,0)
   for j in range(0,100,3):
        fd(120-j)                   
        lt(j) 

############## start the Main #################
main()


