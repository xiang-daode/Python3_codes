from turtle import *
  
# 变色S形曲线:
pensize(6)

for j in range(-360,366,6):
    u=j*j/(360*360)
    pencolor(1-u,u/2,u)
    fd(25)                   
    lt(180-j)





