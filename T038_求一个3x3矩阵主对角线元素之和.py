# 在这里写上你的代码 :-)

'''
题目038：求一个3*3矩阵主对角线元素之和。
'''
def tm038():
    '''
    【备注】：python中涉及到矩阵相关的问题, 推荐直接用numpy模块
    '''
    # 方法1，常规解法
    a = [[1,2,3],[4,5,6],[7,8,9]]
    s = 0
    n = len(a)
    for i in range(n): # 左上到右下一条线
        s+=a[i][i]
    print(s)

def tm038_1():
    # 方法2，numpy解法
    import numpy as np
    data = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(np.trace(data)) #矩阵主对角线元素之和

tm038()
tm038_1()
