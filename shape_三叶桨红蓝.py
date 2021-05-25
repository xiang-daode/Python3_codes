from  turtle import *
from  tkinter import  *
from  math import *

R=180
r=130
s = Shape("compound")
poly1 = []
for q in range(-180,183,3):
    x=int(R*cos(pi*q/180)*cos(pi*q/60))
    y=int(R*sin(pi*q/180)*cos(pi*q/60))
    poly1.append([x,y])
s.addcomponent(poly1, "red", "red")
poly2 = []
for q in range(-180,183,3):
    x=int(r*cos(pi*q/180)*cos(pi*q/60))
    y=int(r*sin(pi*q/180)*cos(pi*q/60))
    poly2.append([x,y])
s.addcomponent(poly2, "blue", "blue")






register_shape("myshape", s)
shape("myshape")
