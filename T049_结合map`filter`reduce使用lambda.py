# 在这里写上你的代码 :-)
'''
题目049：结合map`filter`reduce使用lambda来创建匿名函数。
'''
def tm049():
    '''
    【备注】：lambda函数常常用于建立单行代码的匿名函数。
    '''
    #lambda函数也叫匿名函数，即，函数没有具体的名称。先来看一个最简单例子：
    def f(x):
        return x**2
    print(f(4))

    #Python中使用lambda的话，写成这样
    g = lambda x:x**2
    print(g(4))

    #lambda存在意义就是对简单函数的简洁表示。
    #lambda语句中，冒号前是参数，可以有N个，用逗号隔开，冒号右边的返回值。
    #常搭配内置函数map、filter、reduce，都是应用于序列的内置函数。常见的序列包括list、tuple、str。
    #map(func, *iterables) --> map object
    #filter(function or None, iterable) --> filter object
    #reduce(function, sequence[, initial]) -> value

    #列表数据作示例:
    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

    #按表达式对列表foo各元素xi进行映射到新值(xi * 2 + 10),返回新的列表:
    print(list(map(lambda x: x * 2 + 10, foo)))       # 映射 [14, 46, 28, 54, 44, 58, 26, 34, 64]

    #按判别式(是3的倍数?)对列表foo各元素xi进行筛选,返回新的列表:
    print(list(filter(lambda x: x % 3 == 0, foo)))    # 过滤 [18, 9, 24, 12, 27]

    #reduce_1:各元素之和:
    from functools import reduce                      # 在Python3里,reduce()函数已经被从全局名字空间里移除了,它现在被放置在fucntools模块里
    print(sum(foo),reduce(lambda x, y: x + y, foo))            # 累计求和=139 ,如同: sum(foo)

    #reduce_2:按表达式计算:
    print(2*sum(foo)-foo[0],reduce(lambda x, y: x + 2*y, foo))    # 累计求和=276 ,如同: 2*sum(foo)-foo[0]

    '''
    描述
        reduce() 函数会对参数序列中元素进行累计。
        函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
        用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
        得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
    '''
tm049()

