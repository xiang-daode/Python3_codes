# 在这里写上你的代码 :-)
'''
题目061：打印出杨辉三角形（要求打印出10行如下图）。
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
'''
def tm061():
    '''
    【备注】：配合使用加法的
    '''
    arr = [1]
    print(1)
    while len(arr)<10:                           # [1,1]
        a = [0]+arr                              # [0,1,1]
        b = arr+[0]                              # [1,1,0]
        arr = [a[i]+b[i] for i in range(len(a))] # [1,2,1]
        s = [str(i) for i in arr]
        print(' '.join(s))

tm061()
