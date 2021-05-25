from  turtle import *
from  tkinter import  *
from  math import *

R=250

s = Shape("compound")
poly1 = []
for q in range(-180,183,3):
    poly1.append([int(R*cos(pi*q/120)),int(R*sin(pi*q/150))])
s.addcomponent(poly1, "red", "red")

register_shape("myshape", s)
shape("myshape")
