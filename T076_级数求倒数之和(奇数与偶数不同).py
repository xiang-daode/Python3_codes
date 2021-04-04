# 在这里写上你的代码 :-)
'''
题目076：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''
def tm076():
    n =int(input('请输入一个整数:'))
    ls = sum([1/i for i in range(n,0,-2)])
    print(ls)

tm076()

#注意直接生成列表或集合的写法:
print([x*x for x in range(10)])
print([1/x for x in range(10,0,-1)])
print({x*x for x in range(20,0,-2)})
print({x**x for x in range(10)})
