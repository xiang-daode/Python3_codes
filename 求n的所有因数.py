# 输出n的所有因数

def ys(x):
    for i in range(x-1,1,-1):
        if x%i==0:
            print(i)

n=int(input())
ys(n)