import turtle
turtle.color("purple")    #画笔颜色为紫色
turtle.penup()
turtle.goto(0, -250)
turtle.pendown()
turtle.begin_fill()       #开始填充
turtle.fillcolor("gray")  #填充灰色
turtle.circle(250, steps=4)
turtle.end_fill()         #填充结束
