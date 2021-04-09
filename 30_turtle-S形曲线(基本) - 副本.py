from turtle import *
  
# 双色中国结:
pensize(6)

for j in range(-120,120,3):
    if j>0:pencolor(1,0,0)
    if j<0:pencolor(0,0,1)
    fd(40)                   
    lt(3*j % 180)

for j in range(-90,90,1):
    if j>0:pencolor(1,0,0)
    if j<0:pencolor(0,0,1)
    fd(30)                   
    lt(5*j % 90)





