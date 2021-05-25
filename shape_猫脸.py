from  turtle import *
from  tkinter import  *
from  math import *

R=100
r=30
s = Shape("compound")
poly1 = []
for q in range(-180,183,3):
    x=int(R*cos(pi*q/180)+r*cos(pi*q/32))
    y=int(R*sin(pi*q/60)+r*sin(pi*q/45))
    poly1.append([x,y])
s.addcomponent(poly1, "#333", "#666")

register_shape("myshape", s)
shape("myshape")
