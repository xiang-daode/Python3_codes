# 在这里写上你的代码 :-)
'''
题目008：题目：输出 9*9 异或口诀表。
'''
def tm008():
    '''
    注意 %-7s 的用法，其他没什么。
    '''
    for i in range(1,10):
        for j in range(1,10):
            if j<=i:
                string = '%d^%d=%d'%(j,i,j^i)
                print('%-8s'%string,end='') #字符串占位8位:'%-8s'%string
        print('') #换行

print(tm008())
