from turtle import *
import math

def main():
   width(5);pencolor(1,0,0)
   #N个三角形:
   for i in range(0,360,30):
      pu()
      x=200*math.cos(3.1416*i/180)
      y=200*math.sin(3.1416*i/180)
      goto(x,y)
      
      pd();pencolor(1,i/360,1-i/360)
      for j in range(0,3):               
           rt(-120)
           fd(100)  

############## start the Main #################
main()


