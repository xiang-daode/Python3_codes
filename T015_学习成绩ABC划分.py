# 在这里写上你的代码 :-)
'''
题目015：利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
'''
def tm015():
    '''
    【备注】：if-else基本用法
    '''
    score = float(input('输入一个成绩:'))
    if score>=90:
        print('A')
    elif score>=60:
        print('B')
    else:
        print('C')

tm015()

