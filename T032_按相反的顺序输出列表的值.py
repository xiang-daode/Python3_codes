# 在这里写上你的代码 :-)
'''
题目032：按相反的顺序输出列表的值。
'''
def tm032():
    '''
    【备注】：
    '''
    # 方法一,利用下标递减
    a = [1,2,9,4,5]
    print(a[::-1])

    # 方法二,使用内置函数
    a = [1,2,9,4,5]
    a.reverse()
    print(a)

    # 方法三,排序[逆序],有时正确
    a = [1,2,9,4,5]
    a.sort(reverse=True)
    print(a)

tm032()
