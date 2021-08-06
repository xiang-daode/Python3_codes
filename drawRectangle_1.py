# draw Rectangle in Python Turtle
import turtle
t = turtle.Turtle()

def drawRect(w,l):
    for _ in range(4):
      # drawing length
      if _% 2 == 0:
        t.forward(l)
        t.left(90)
      else:
        t.forward(w)
        t.left(90)

drawRect(123,45)
