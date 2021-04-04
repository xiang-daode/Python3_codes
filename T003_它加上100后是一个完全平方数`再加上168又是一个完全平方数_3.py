# 在这里写上你的代码 :-)

'''
题目003：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''

def tm003_1():
    '''
    如果不想使用开方函数，也可以使用Xueyang_Liu的方法也行。根据之前的推论x<=83.5，所以实际取值范围可以写成x<84。
    '''
    arr=[]
    result=[]
    for i in range(84):
        arr+=[i**2]
    for elem in arr:
        if elem+168 in arr:
            result+=[elem-100]
    return result

print(tm003_1()  )
