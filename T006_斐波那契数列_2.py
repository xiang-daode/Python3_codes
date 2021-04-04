# 在这里写上你的代码 :-)
'''
题目006：斐波那契数列。
'''
def tm006(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return tm006(n-1)+tm006(n-2)

for n in range(33):
    print(tm006(n),end=",")
