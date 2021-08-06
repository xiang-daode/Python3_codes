# draw Rectangle in Python Turtle
import turtle
t = turtle.Turtle()

def drawRect(x,y,w,l,r,g,b):
    t.pencolor(r,g,b)
    t.goto(x,y)
    for _ in range(4):
      # drawing length
      if _% 2 == 0:
        t.forward(l)
        t.left(90)
      else:
        t.forward(w)
        t.left(90)

drawRect(0,0,123,45,1,0,0)
drawRect(120,0,123,45,1,0,0)
