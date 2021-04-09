from turtle import *
  
#画多边形,中心坐标是(0,0),范围是(-375..+375, -275..+275):
pensize(4)

#X轴:
pu(),goto(-375,0)
pencolor(1,1,0)
pd(),goto(375,0)

#Y轴:
pu(),goto(0,-275)
pencolor(1,0,1)
pd(),goto(0,275)

lt=[(200,200),(-200,200),(-200,-200),(200,-200),(200,200)]
pencolor(1,0,0)

pu()
for j in range(len(lt)):   
   if j>0:
      pd()   
   goto(lt[j][0],lt[j][1])


