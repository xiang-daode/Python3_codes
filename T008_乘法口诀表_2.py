# 在这里写上你的代码 :-)

def tm008_1():
    '''
    题目：输出 9*9 乘法口诀表。
	用format方法生成字符串。
    用循环到i+1的方法，比上面还能少写一行。
    {2:2}表示第2个变量占用2字符位置
    '''
    for i in range(1,10):
        for j in range(1, i + 1):
            print(" {0}*{1}={2:2} ".format(i, j, i*j),end=' ')
        print()

print(tm008_1())
