# 在这里写上你的代码 :-)
'''
题目036：求100之内的素数。
'''
def tm036():
    '''
    【备注】：素数就是质数,除了1和本身之外,没有其他的因数
    '''
    arr = [2]
    for i in range(3,100):
        for j in arr:
            if i%j==0:
                break
        else:
            arr.append(i)
    print(arr)

tm036()
