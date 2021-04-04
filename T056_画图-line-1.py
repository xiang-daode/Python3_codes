# 在这里写上你的代码 :-)
'''
【备注】：#画line,线粗4,背景色: #ddeeff
'''
import tkinter

def tm056_1():

    canvas = tkinter.Canvas(width=600, height=500, bg='#ddeeff')
    canvas.pack(expand='yes', fill='both')
    r=150
    canvas.create_line(300 - r,250 - r,300 + r,250 + r, width=4)
    canvas.mainloop()
tm056_1()
