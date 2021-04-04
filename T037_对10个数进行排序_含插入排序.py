# 在这里写上你的代码 :-)
'''
题目037：对10个数进行排序。
'''
def tm037():
    '''
    【个人备注】：实际上考察的是排序。揣测了一下题意，写了两种解法
    '''
    # 方法1，python解法
    a = [1,5,7,3,2,4,9,10,6,8]
    a.sort()
    print(a)

    # 方法2，常规解法_插入法
    a = [1,5,7,3,2,4,9,10,6,8]
    b = [a[0]]
    for num in a[1:]:
        for i in range(len(b)):
            if num<b[i]:
                b.insert(i,num)
                break
        else:
            b.append(num)
    print(b)

tm037()
