# 在这里写上你的代码 :-)
'''
题目023_图案: 图案:近似圆


'''
def tm023():
    '''
    【备注】：近似圆图案,使用了勾股定理
    '''
    import math
    D = 20
    r=D/2
    for i in range(D):
        d=i-D/2 #-10...+10
        w=int(pow(r*r-d*d,0.5))
        print(' '*(D-2*w)+'****'*w)
tm023()
