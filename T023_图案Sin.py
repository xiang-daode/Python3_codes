# 在这里写上你的代码 :-)
'''
题目023_图案:三角函数sin()图案
打印出如下图案（）:

'''
def tm023():
    '''
    【备注】：三角函数sin()图案
    '''
    import math
    num = 60
    for i in range(num):
        blank = int(25+20*math.sin(3.1416*i*3/90))
        print(' '*blank+'@')
tm023()
