from turtle import *
import math

def main(): 
  
   fd(200); lt(90)
   
   #circle:
   for i in range(0,360,10):                
        lt(10); fd(2*200*3.1416/36)
        
   #4-sides:
   for j in range(0,360,90):
        fd(100)                   
        lt(90);
        
   #6-sides:
   lt(30)  
   for j in range(0,360,60):
        fd(80)                   
        lt(60); 

############## start the Main #################
main()


