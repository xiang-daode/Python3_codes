from  turtle import *
from  tkinter import  *
from  math import *

R=250

s = Shape("compound")
poly1 = []
for q in range(-180,183,3):
    poly1.append([int(R*sin(pi*q/180)),int(R*cos(pi*q/180))])
s.addcomponent(poly1, "red", "blue")

R=R/2
poly2 = []
for q in range(-180,183,3):
    poly2.append([int(R*sin(pi*q/180)),int(R*cos(pi*q/180))])
s.addcomponent(poly2, "blue", "red")

R=R/2
poly3 = []
for q in range(-180,183,3):
    poly3.append([int(R*sin(pi*q/180)),int(R*cos(pi*q/180))])
s.addcomponent(poly3, "green", "black")


register_shape("myshape", s)
shape("myshape")
