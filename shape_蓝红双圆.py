from  turtle import *
from  tkinter import  *
from  math import *
PI=3.14159265
R=120

s = Shape("compound")
poly1 = []
for q in range(-180,183,3):
    poly1.append([int(R*sin(PI*q/180)),int(R*cos(PI*q/180)-R)])

s.addcomponent(poly1, "red", "blue")


poly2 = []
for q in range(-180,183,3):
    poly2.append([int(R*sin(PI*q/180)),int(R*cos(PI*q/180)+R)])

s.addcomponent(poly2, "blue", "red")


register_shape("myshape", s)
shape("myshape")
