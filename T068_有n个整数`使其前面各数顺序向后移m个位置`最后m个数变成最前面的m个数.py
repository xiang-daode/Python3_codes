# 在这里写上你的代码 :-)
'''
题目068：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''
def tm068():
    a = [1,2,3,4,5,6,7,8,9,10]
    for m in range(10):
        b = a[-m:]+a[:-m]
        print(b)

tm068()
