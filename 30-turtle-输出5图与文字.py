import turtle

#
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.begin_fill()    #开始填充
turtle.color("black")  #填充黑色
turtle.circle(40)
turtle.end_fill()      #填充结束

#
turtle.color("red")    #画笔颜色为红色
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps=3)

#
turtle.color("purple")    #画笔颜色为紫色
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill()       #开始填充
turtle.fillcolor("gray")  #填充灰色
turtle.circle(40, steps=4)
turtle.end_fill()         #填充结束

#
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill()        #开始填充
turtle.fillcolor("yellow") #fillcolor为黄色
turtle.color("purple")     #color为紫色
turtle.circle(40, steps=5)
turtle.end_fill()          #填充结束

#
turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill()        #开始填充
turtle.color("yellow")     #color为黄色
turtle.fillcolor("green")  #fillcolor为绿色
turtle.circle(40, steps=6)
turtle.end_fill()          #填充结束


#
turtle.color("blue")
turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()
turtle.write("Colorful Shapes", font = ("Times", 18, "bold"))
#
turtle.penup();
turtle.goto(0, 250);
turtle.pendown()
turtle.write("完成", font = ("黑体", 18, "bold"))


#隐藏箭头
turtle.hideturtle()
#暂停界面，使得用户能够看见展示的图形
turtle.done()
