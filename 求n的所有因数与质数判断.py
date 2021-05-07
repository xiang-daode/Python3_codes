# 输出n的所有因数

def ys(x):
    for i in range(x-1,1,-1):
        if x%i==0:
            print(i)

n=int(input("输入一个正整数: ","288"))


def isPrime(x):
    prime=True
    for i in range(x-1,1,-1):
        if x%i==0:
            prime=False
    return prime        

ys(n)
tf=isPrime(n)
print(tf)
