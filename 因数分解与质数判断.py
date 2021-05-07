# 自定义函数, factorization---因数分解:
def fact(x):
    for i in range(x-1,1,-1):
        if x%i==0:
            print(i)

#让用户输入一个正整数:
n=int(input("输入一个正整数[将列出它的所有因数]: "))
#调用自己编的函数:
fact(n)
























# isPrime ?---素数(质数)判断
def isPrime(x):
    prime=True
    for i in range(2,x-1):
        if x%i==0:
            prime=False
    return prime

#让用户输入一个正整数:
n=int(input("输入一个正整数[将列出它的所有因数]: "))
tf=isPrime(n)
print(tf)

#100---999(包含999)内的所有质数:
for i in range(100,1000):
    if isPrime(i):
        print(i,end=',')
