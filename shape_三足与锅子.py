from  turtle import *
from  tkinter import  *
from  math import *

R=250

s = Shape("compound")
poly1 = []
for q in range(-180,183,3):
    x=int(R*cos(pi*q/120)*cos(pi*q/40))
    y=int(R*sin(pi*q/150)*cos(pi*q/40))
    poly1.append([x,y])
s.addcomponent(poly1, "red", "red")

register_shape("myshape", s)
shape("myshape")
