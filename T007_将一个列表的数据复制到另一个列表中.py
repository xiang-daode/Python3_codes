# 在这里写上你的代码 :-)
'''
题目007：将一个列表的数据复制到另一个列表中。
'''
def tm007():
    '''
    【个人备注】：如果系统的看过python教程之类的应该都知道。
    Python里面一切都是对象，list的复制需要用a[:]或a.copy()的方式。
    至于b=a只是相当于给a取了个别名而已，指向的是同一个列表，并没有实现复制。
    '''
    a = [1, 2, 3]
    b = a[:]
    c=a.copy()
    '''题外话'''
    a[0]=0
    c[0]=999
    print(id(a),id(b),id(c))  # 可以看到a,b的内存不一致，是复制
    print(a,b,c)          # 修改a之后b不变
    a = [1, 2, 3]
    b = a
    a[0]=0
    print(id(a),id(b))  # 如果去掉[:]，可以看到a,b的内存一致，并没有复制，指向的是同一个列表
    print(a,b)          # 修改a之后b也变

print(tm007())
