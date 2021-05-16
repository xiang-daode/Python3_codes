from turtle import *

pencolor("#ff2288")
pensize(6)
for j in range(0,460,5):
    fd(6)
    lt(5)
for j in range(0,360,5):
    fd(8)
    rt(5)
pencolor("#6622ff")
for j in range(0,260,5):
    fd(6+j/70)
    lt(j/5)
pencolor("#66ff88")
for j in range(0,160,5):
    fd(8-j/80)
    rt(j/3)





