# 在这里写上你的代码 :-)
'''
题目019：一个数如果恰好等于它的因数之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''
def tm019():
    '''
    【个人备注】：题意看的不是太懂，于是百度了一下：完数就是除了自身之外的所有约数之和等于他本身。
    第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6。
    第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
    终于看懂了题意。
    先求出所有约数，然后求和比一下是否相等就行了，没有难度
    '''
    for num in range(1,1000):
        arr = []
        for i in range(1,num):
            if num%i==0:
                arr.append(i)
        if sum(arr)==num:
            print(num,arr)

tm019()
