# draw Rectangle in Python Turtle
import turtle
t = turtle.Turtle()

def drawRect(x,y,w,l,r,g,b):
    t.color(r,g,b);t.pu()
    t.goto(x,y);t.pd()
    t.begin_fill()
    for _ in range(4):
      if _% 2 == 0:
        t.forward(l)
        t.left(90)
      else:
        t.forward(w)
        t.left(90)
    t.end_fill()

drawRect(-200,-300,223,45,1,0,0)
drawRect(-100,-300,273,45,0,1,0)
drawRect(0,-300,293,45,0,1,0)
drawRect(100,-300,273,45,0,1,1)
drawRect(200,-300,253,45,1,1,0)
