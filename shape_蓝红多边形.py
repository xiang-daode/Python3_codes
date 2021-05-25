from  turtle import *
from  tkinter import  *


s = Shape("compound")
poly1 = [[0,0],[120,-150],[0,120],[-120,-150]]
s.addcomponent(poly1, "red", "blue")


poly2 = [[0,180],[-50,100],[50,100]]
s.addcomponent(poly2, "blue", "red")


register_shape("myshape", s)
shape("myshape")
