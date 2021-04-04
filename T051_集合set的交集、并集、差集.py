# 在这里写上你的代码 :-)
'''
题目051_集合set的交集、并集、差集
'''
def tm051():
    '''
    【备注】：集合的交集、并集、差集
    '''
    # 可迭代变量转换为集合形式:
    x = set('runoob')
    y = set('google')
    print(x, y)          # 重复的已经被删除 {'n', 'o', 'b', 'u', 'r'} {'o', 'g', 'e', 'l'}

    # 集合的交集、并集、差集:
    print(x & y)         # 交集 {'o'}
    print(x | y)         # 并集 {'e', 'o', 'g', 'l', 'u', 'n', 'b', 'r'}
    print(x - y)         # 差集 {'n', 'b', 'u', 'r'}

    # 当然也可以写成函数形式，不过确实没有上面符号好记:
    print(x.intersection(y))
    print(x.union(y))
    print(x.difference(y))

tm051()


