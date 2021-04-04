# 在这里写上你的代码 :-)
'''
题目056：画图，学用circle画圆形。
题目057：画图，学用line画直线。
题目058：画图，学用rectangle画方形。
题目059：画图，综合例子。
题目063：画椭圆。
题目064：利用ellipse 和 rectangle 画图。
题目065：一个最优美的图案。
'''
def tm056(): # tm057、tm058、tm059、tm063、tm064、tm065、
    '''
    【备注】：#画半径是150的圆,线粗4,背景色: #ddeeff
    '''
    import tkinter
    canvas = tkinter.Canvas(width=600, height=500, bg='#ddeeff')
    canvas.pack(expand='yes', fill='both')
    r=150
    canvas.create_oval(300 - r,250 - r,300 + r,250 + r, width=4)

    canvas.mainloop()

tm056()
