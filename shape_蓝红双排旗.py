from  turtle import *
from  tkinter import  *


s = Shape("compound")
poly1 = []
for q in range(-100,100,3):
    poly1.append([q,q%60+80])

s.addcomponent(poly1, "red", "blue")


poly2 = []
for q in range(-180,180,3):
    poly2.append([q,q%60-80])

s.addcomponent(poly2, "blue", "red")


register_shape("myshape", s)
shape("myshape")
