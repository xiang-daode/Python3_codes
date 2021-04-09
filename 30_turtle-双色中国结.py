from turtle import *
  
# 双色中国结:
pensize(6)

for j in range(-120,120,6):
    if j>0:pencolor(1,0,0)
    if j<0:pencolor(0,0,1)
    fd(40-j/20)                   
    lt(3*j % 90)






